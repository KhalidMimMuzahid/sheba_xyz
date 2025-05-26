
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from modules.users.schemas import UserCreateRequest,  UserCreateResponse
from modules.users.services import create_user
from database import get_db 
from responses.handler import create_response
from responses.models import Response
user_router = APIRouter()



@user_router.post("/register-user", response_model=Response[UserCreateResponse])
async def register_user_(user:UserCreateRequest, db: AsyncSession = Depends(get_db)):
    result =  await create_user(db= db, email= user.email, name=user.name, password=user.password)
    return create_response(result=result, pydantic_model=UserCreateResponse, message="User has registered successfully")