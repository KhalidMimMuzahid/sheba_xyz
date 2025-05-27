from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum


# Define an enumeration for role type
class UserRoleEnum(enum.Enum):
    admin = "admin"
    # user =  "user"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(UserRoleEnum), nullable=False, default= "admin")
    name = Column(String,  unique=False, index=True)
    password = Column(String, nullable=False)