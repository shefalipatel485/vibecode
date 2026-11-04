from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

class RegisterIn(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8)
    role: str = "customer"
    phone: Optional[str] = None

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class ServiceIn(BaseModel):
    name: str
    category: str
    description: str = ""
    price: float = Field(ge=0)
    duration_minutes: int = Field(default=60, ge=15)
    provider_id: Optional[int] = None

class BookingIn(BaseModel):
    service_id: int
    provider_id: int
    appointment_at: str
    address: str
    problem_description: str = ""

class StatusIn(BaseModel):
    status: str

class AssignIn(BaseModel):
    technician_id: int

class PaymentIn(BaseModel):
    method: str = "Demo payment"

class ReviewIn(BaseModel):
    rating: int = Field(ge=1, le=5)
    comment: str = ""

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    is_approved: bool
