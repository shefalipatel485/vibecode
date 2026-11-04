import os
from datetime import datetime, timedelta, timezone
import jwt
from pwdlib import PasswordHash

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-this-secret-before-deployment")
ALGORITHM = "HS256"
TOKEN_MINUTES = int(os.getenv("ACCESS_TOKEN_MINUTES", "1440"))
password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return password_hash.verify(password, hashed)

def create_access_token(user_id: int, role: str):
    expires = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_MINUTES)
    return jwt.encode({"sub": str(user_id), "role": role, "exp": expires}, SECRET_KEY, algorithm=ALGORITHM)
