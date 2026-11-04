import os, uuid
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from sqlalchemy import func
import jwt
from jwt import InvalidTokenError
from .database import Base, engine, get_db
from .models import User, Service, Booking, Review
from .schemas import RegisterIn, LoginIn, ServiceIn, BookingIn, StatusIn, AssignIn, PaymentIn, ReviewIn
from .security import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM
from .seed import seed

app = FastAPI(title="HomeServe SaaS API", version="1.0.0",
              description="Home services booking capstone API")
origins = [x.strip() for x in os.getenv("FRONTEND_ORIGINS", "http://localhost:5173").split(",") if x.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])
bearer = HTTPBearer(auto_error=False)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    from .database import SessionLocal
    db = SessionLocal()
    try: seed(db)
    finally: db.close()

def current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer),
                 db: Session = Depends(get_db)):
    if not credentials: raise HTTPException(401, "Authentication required")
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub", 0))
    except (InvalidTokenError, ValueError):
        raise HTTPException(401, "Invalid or expired token")
    user = db.get(User, user_id)
    if not user or not user.is_active: raise HTTPException(401, "User not available")
    return user

def allow(*roles):
    def checker(user: User = Depends(current_user)):
        if user.role not in roles: raise HTTPException(403, "You do not have permission")
        return user
    return checker

def user_data(u):
    return {"id":u.id,"name":u.name,"email":u.email,"role":u.role,
            "phone":u.phone,"is_active":u.is_active,"is_approved":u.is_approved}

def service_data(s):
    return {"id":s.id,"name":s.name,"category":s.category,"description":s.description,
            "price":s.price,"duration_minutes":s.duration_minutes,"provider_id":s.provider_id}

def booking_data(b, db):
    service = db.get(Service, b.service_id)
    customer = db.get(User, b.customer_id)
    provider = db.get(User, b.provider_id)
    tech = db.get(User, b.technician_id) if b.technician_id else None
    return {"id":b.id,"booking_code":b.booking_code,"customer_id":b.customer_id,
            "customer_name":customer.name if customer else "","provider_id":b.provider_id,
            "provider_name":provider.name if provider else "","technician_id":b.technician_id,
            "technician_name":tech.name if tech else None,"service_id":b.service_id,
            "service_name":service.name if service else "","appointment_at":b.appointment_at,
            "address":b.address,"problem_description":b.problem_description,"status":b.status,
            "payment_status":b.payment_status,"amount":b.amount}

@app.get("/health")
def health(): return {"status":"ok","service":"HomeServe API"}

@app.post("/auth/register")
def register(data: RegisterIn, db: Session = Depends(get_db)):
    if data.role not in ("customer","provider","technician"):
        raise HTTPException(400,"Choose customer, provider or technician")
    if db.query(User).filter(func.lower(User.email)==data.email.lower()).first():
        raise HTTPException(409,"Email already registered")
    user = User(name=data.name,email=data.email.lower(),password_hash=hash_password(data.password),
                role=data.role,phone=data.phone,is_active=True,is_approved=(data.role!="provider"))
    db.add(user); db.commit(); db.refresh(user)
    return {"message":"Registration successful. Provider accounts require admin approval.",
            "user":user_data(user)}

@app.post("/auth/login")
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(func.lower(User.email)==data.email.lower()).first()
    if not user or not verify_password(data.password,user.password_hash):
        raise HTTPException(401,"Invalid email or password")
    if not user.is_active: raise HTTPException(403,"Account is inactive")
    return {"access_token":create_access_token(user.id,user.role),"token_type":"bearer","user":user_data(user)}

@app.get("/auth/me")
def me(user: User = Depends(current_user)): return user_data(user)

@app.get("/users")
def users(db: Session=Depends(get_db), admin: User=Depends(allow("admin"))):
    return [user_data(u) for u in db.query(User).order_by(User.created_at.desc()).all()]

@app.patch("/users/{user_id}/approval")
def approval(user_id:int, approved:bool, db:Session=Depends(get_db), admin:User=Depends(allow("admin"))):
    u=db.get(User,user_id)
    if not u or u.role!="provider": raise HTTPException(404,"Provider not found")
    u.is_approved=approved; db.commit()
    return {"message":"Provider approval updated","user":user_data(u)}

@app.get("/services")
def services(category:str|None=None, q:str|None=None, db:Session=Depends(get_db)):
    query=db.query(Service).filter(Service.active==True)
    if category: query=query.filter(Service.category==category)
    if q: query=query.filter(Service.name.ilike(f"%{q}%"))
    return [service_data(s) for s in query.order_by(Service.id.desc()).all()]

@app.post("/services")
def create_service(data:ServiceIn, db:Session=Depends(get_db), user:User=Depends(allow("admin","provider"))):
    provider_id = data.provider_id if user.role=="admin" and data.provider_id else user.id
    if user.role=="provider" and not user.is_approved: raise HTTPException(403,"Provider is awaiting approval")
    s=Service(**data.model_dump(exclude={"provider_id"}),provider_id=provider_id)
    db.add(s); db.commit(); db.refresh(s)
    return service_data(s)

@app.put("/services/{service_id}")
def update_service(service_id:int,data:ServiceIn,db:Session=Depends(get_db),user:User=Depends(allow("admin","provider"))):
    s=db.get(Service,service_id)
    if not s: raise HTTPException(404,"Service not found")
    if user.role=="provider" and s.provider_id!=user.id: raise HTTPException(403,"Not your service")
    for k,v in data.model_dump(exclude={"provider_id"}).items(): setattr(s,k,v)
    db.commit(); db.refresh(s); return service_data(s)

@app.delete("/services/{service_id}")
def delete_service(service_id:int,db:Session=Depends(get_db),user:User=Depends(allow("admin","provider"))):
    s=db.get(Service,service_id)
    if not s: raise HTTPException(404,"Service not found")
    if user.role=="provider" and s.provider_id!=user.id: raise HTTPException(403,"Not your service")
    s.active=False; db.commit(); return {"message":"Service deactivated"}

@app.post("/bookings")
def create_booking(data:BookingIn,db:Session=Depends(get_db),user:User=Depends(allow("customer"))):
    service=db.get(Service,data.service_id); provider=db.get(User,data.provider_id)
    if not service or not service.active: raise HTTPException(404,"Service unavailable")
    if service.provider_id != data.provider_id: raise HTTPException(400,"Selected provider does not offer this service")
    if not provider or provider.role!="provider" or not provider.is_approved: raise HTTPException(400,"Provider is not available")
    b=Booking(booking_code="HS-"+uuid.uuid4().hex[:8].upper(),customer_id=user.id,
              provider_id=data.provider_id,service_id=service.id,appointment_at=data.appointment_at,
              address=data.address,problem_description=data.problem_description,amount=service.price)
    db.add(b); db.commit(); db.refresh(b); return booking_data(b,db)

@app.get("/bookings")
def bookings(db:Session=Depends(get_db),user:User=Depends(current_user)):
    q=db.query(Booking)
    if user.role=="customer": q=q.filter(Booking.customer_id==user.id)
    elif user.role=="provider": q=q.filter(Booking.provider_id==user.id)
    elif user.role=="technician": q=q.filter(Booking.technician_id==user.id)
    return [booking_data(b,db) for b in q.order_by(Booking.created_at.desc()).all()]

@app.patch("/bookings/{booking_id}/status")
def booking_status(booking_id:int,data:StatusIn,db:Session=Depends(get_db),user:User=Depends(current_user)):
    allowed={"Pending","Confirmed","Assigned","In Progress","Completed","Cancelled","Rejected"}
    if data.status not in allowed: raise HTTPException(400,"Invalid booking status")
    b=db.get(Booking,booking_id)
    if not b: raise HTTPException(404,"Booking not found")
    permitted=(user.role=="admin" or (user.role=="customer" and b.customer_id==user.id and data.status=="Cancelled")
               or (user.role=="provider" and b.provider_id==user.id and data.status in {"Confirmed","Rejected","In Progress","Completed"})
               or (user.role=="technician" and b.technician_id==user.id and data.status in {"In Progress","Completed"}))
    if not permitted: raise HTTPException(403,"Not permitted to change this booking")
    b.status=data.status; db.commit(); return booking_data(b,db)

@app.patch("/bookings/{booking_id}/assign")
def assign_technician(booking_id:int,data:AssignIn,db:Session=Depends(get_db),user:User=Depends(current_user)):
    b=db.get(Booking,booking_id)
    if not b: raise HTTPException(404,"Booking not found")
    if user.role not in ("admin","provider") or (user.role=="provider" and b.provider_id!=user.id):
        raise HTTPException(403,"Not permitted")
    tech=db.get(User,data.technician_id)
    if not tech or tech.role!="technician" or not tech.is_active: raise HTTPException(400,"Technician not found")
    b.technician_id=tech.id; b.status="Assigned"; db.commit(); return booking_data(b,db)

@app.post("/bookings/{booking_id}/pay")
def pay(booking_id:int,data:PaymentIn,db:Session=Depends(get_db),user:User=Depends(allow("customer"))):
    b=db.get(Booking,booking_id)
    if not b or b.customer_id!=user.id: raise HTTPException(404,"Booking not found")
    if b.status in ("Cancelled","Rejected"): raise HTTPException(400,"Cannot pay for cancelled/rejected booking")
    b.payment_status="Paid"; db.commit()
    return {"message":"Demo payment successful (no real money charged)","booking":booking_data(b,db)}

@app.post("/bookings/{booking_id}/reviews")
def review(booking_id:int,data:ReviewIn,db:Session=Depends(get_db),user:User=Depends(allow("customer"))):
    b=db.get(Booking,booking_id)
    if not b or b.customer_id!=user.id: raise HTTPException(404,"Booking not found")
    if b.status!="Completed": raise HTTPException(400,"Review allowed after completion")
    if db.query(Review).filter_by(booking_id=b.id).first(): raise HTTPException(409,"Review already submitted")
    r=Review(booking_id=b.id,customer_id=user.id,provider_id=b.provider_id,rating=data.rating,comment=data.comment)
    db.add(r); db.commit(); return {"message":"Review submitted"}

@app.get("/reviews")
def reviews(db:Session=Depends(get_db),user:User=Depends(current_user)):
    q=db.query(Review)
    if user.role=="provider": q=q.filter(Review.provider_id==user.id)
    return [{"id":r.id,"booking_id":r.booking_id,"rating":r.rating,"comment":r.comment,
             "customer_name":db.get(User,r.customer_id).name} for r in q.order_by(Review.created_at.desc()).all()]

@app.get("/dashboard")
def dashboard(db:Session=Depends(get_db),user:User=Depends(current_user)):
    if user.role=="admin":
        return {"customers":db.query(User).filter_by(role="customer").count(),
                "providers":db.query(User).filter_by(role="provider").count(),
                "technicians":db.query(User).filter_by(role="technician").count(),
                "bookings":db.query(Booking).count(),
                "pending":db.query(Booking).filter_by(status="Pending").count(),
                "completed":db.query(Booking).filter_by(status="Completed").count(),
                "revenue":db.query(func.sum(Booking.amount)).filter_by(payment_status="Paid").scalar() or 0}
    q=db.query(Booking)
    if user.role=="customer": q=q.filter_by(customer_id=user.id)
    elif user.role=="provider": q=q.filter_by(provider_id=user.id)
    elif user.role=="technician": q=q.filter_by(technician_id=user.id)
    rows=q.all()
    return {"bookings":len(rows),"pending":sum(b.status=="Pending" for b in rows),
            "completed":sum(b.status=="Completed" for b in rows),
            "revenue":sum(b.amount for b in rows if b.payment_status=="Paid")}
