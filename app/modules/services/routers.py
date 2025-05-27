
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db 
from modules.services.services import create_service, get_services, delete_service, update_service
from responses.models import Response
from responses.handler import create_response
from modules.services.schemas import ServiceCreateRequest, ServiceCreateResponse, ServiceListResponse, ServiceUpdateRequest



service_router = APIRouter()

@service_router.post("/add-service", response_model=  Response[ServiceCreateResponse]
)
async def add_service(service: ServiceCreateRequest, db: AsyncSession = Depends(get_db)):
    result= await create_service(db=db, name= service.name, category= service.category, description= service.description, price=service.price )
    return create_response(result=result, pydantic_model=ServiceCreateResponse, message="Service has added successfully")


@service_router.get("/get-services"
, response_model=Response[list[ServiceListResponse]]
)
async def list_services(page:int=1, limit:int=10, category:str=None, db: AsyncSession = Depends(get_db)):
    result= await get_services(db, page, limit, category)
    return create_response(result=result["data"], pydantic_model=ServiceListResponse, message="Services have retrieved successfully", meta_data=result["meta_data"] )
    
@service_router.delete("/delete-service"
)
async def delete_service_(id:int, db: AsyncSession = Depends(get_db)):
    result= await delete_service(db, id)
    return create_response(result=result,  message="Service has deleted successfully successfully" )


@service_router.put("/update-service", response_model=Response[ServiceUpdateRequest])
async def update_service_(
    service_id: int,
    name: str=None,
    category: str=None,
    description:str=None,
    price: int=None,
    db: AsyncSession = Depends(get_db)
):
    result = await update_service(
        db=db,
        service_id=service_id,
        name= name,
        category= category,
        description=description,
        price=price,
    )
    return create_response(result=result, pydantic_model=ServiceUpdateRequest, message="Service updated successfully")
