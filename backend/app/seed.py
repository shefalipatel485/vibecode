from sqlalchemy.orm import Session
from .models import User, Service
from .security import hash_password

DEMO_PASSWORD = "Demo@123"

def seed(db: Session):
    accounts = [
        ("HomeServe Admin", "admin@homeserve.demo", "admin", True),
        ("Demo Customer", "customer@homeserve.demo", "customer", True),
        ("Demo Provider", "provider@homeserve.demo", "provider", True),
        ("Demo Technician", "technician@homeserve.demo", "technician", True),
    ]
    for name, email, role, approved in accounts:
        if not db.query(User).filter_by(email=email).first():
            db.add(User(name=name, email=email, role=role,
                        password_hash=hash_password(DEMO_PASSWORD),
                        is_active=True, is_approved=approved))
    db.commit()
    provider = db.query(User).filter_by(email="provider@homeserve.demo").first()
    samples = [
        ("Electrical Repair", "Electrical Services", "Switch, wiring and fan repairs by a qualified professional.", 499, 60),
        ("Plumbing Service", "Plumbing Services", "Tap, leakage and bathroom plumbing solutions.", 399, 60),
        ("AC Service", "AC Repair & Maintenance", "Routine AC cleaning and maintenance.", 799, 90),
        ("Home Deep Cleaning", "Home Cleaning", "Deep cleaning for rooms, kitchen and bathrooms.", 1499, 180),
        ("Carpentry Repair", "Carpentry Services", "Door, furniture and cabinet repairs.", 599, 60),
        ("Appliance Repair", "Appliance Repair", "Diagnosis and repair for common home appliances.", 699, 90),
    ]
    for name, cat, desc, price, duration in samples:
        if not db.query(Service).filter_by(name=name).first():
            db.add(Service(name=name, category=cat, description=desc, price=price,
                           duration_minutes=duration, provider_id=provider.id, active=True))
    db.commit()
