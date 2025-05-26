from datetime import datetime, timedelta
from passlib.context import CryptContext
from config import Config
import jwt
passwd_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRY = 7*24*60*60   # in second


def generate_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)
    return hash

def verify_password(password: str, hash: str) -> bool:
    return passwd_context.verify(password, hash)

def create_access_token(
    user_data: dict, expiry: timedelta = None, refresh: bool = False
):

    payload = {}
    payload["auth"] = user_data
    payload["exp"] = datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    payload["refresh"] = refresh
    token = jwt.encode(
        payload=payload, key=Config.JWT_SECRET, algorithm= Config.JWT_ALGORITHM
    )
    return token