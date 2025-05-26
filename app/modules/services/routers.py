
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db 
from modules.services.services import create_service
from responses.models import Response
from responses.handler import create_response
from app.modules.services.schemas import ServiceCreateRequest, ServiceCreateResponse

service_router = APIRouter()

@service_router.post("/add-service", response_model=  Response[ServiceCreateResponse]
)
async def add_service(service: ServiceCreateRequest, db: AsyncSession = Depends(get_db)):
    result= await create_service(db=db, name= service.name, category= service.category, description= service.description, price=service.price )
    return create_response(result=result, pydantic_model=ServiceCreateResponse, message="Service has added successfully")
