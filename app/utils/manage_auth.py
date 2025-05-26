from datetime import datetime, timedelta

from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRY = 7*24*60*60   # in second


def generate_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)
    return hash
