
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db 
from modules.services.services import create_service, get_services
from responses.models import Response
from responses.handler import create_response
from modules.services.schemas import ServiceCreateRequest, ServiceCreateResponse, ServiceListResponse


service_router = APIRouter()

@service_router.post("/add-service", response_model=  Response[ServiceCreateResponse]
)
async def add_service(service: ServiceCreateRequest, db: AsyncSession = Depends(get_db)):
    result= await create_service(db=db, name= service.name, category= service.category, description= service.description, price=service.price )
    return create_response(result=result, pydantic_model=ServiceCreateResponse, message="Service has added successfully")


@service_router.get("/get-services"
# , response_model=Response[list[ServiceListResponse]]
)
async def list_services(page:int=1, limit:int=10, category:str=None, db: AsyncSession = Depends(get_db)):
    result= await get_services(db, page, limit, category)
    return create_response(result=result["data"], pydantic_model=ServiceListResponse, message="Services have retrieved successfully", meta_data=result["meta_data"] )
    