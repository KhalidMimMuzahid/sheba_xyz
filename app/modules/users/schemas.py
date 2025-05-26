from pydantic import BaseModel
from enum import Enum

# Define an enumeration for Role
class UserRoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserCreateRequest(BaseModel):
    email :str
    name :str
    password :str

class UserCreateResponse(BaseModel):
    id: int
    email :str
    name :str
    role : UserRoleEnum
    # password :str
    class Config:
        orm_mode = True
        extra = "ignore"  # This will ignore any extra fields (like "password")


class UserLogInResponse(BaseModel):
    id: int
    email :str
    role : UserRoleEnum
    name :str
    access_token:str
    class Config:
        orm_mode = True
        extra = "ignore"
