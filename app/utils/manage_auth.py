from datetime import datetime, timedelta
from passlib.context import CryptContext
from app.config import Config
import jwt
passwd_context = CryptContext(schemes=["bcrypt"])
from app.exceptions.models import CustomError

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

def decode_access_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token, key=Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM]
        )
        return token_data
    except jwt.ExpiredSignatureError:
        raise CustomError(message= "your access token has been expired", status_code=401, resolution="please sign in again.")
    except jwt.InvalidTokenError:
        raise CustomError(message= "your access token is invalid", status_code=401, resolution="please provide a valid token.")
