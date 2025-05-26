from fastapi import APIRouter
from modules.services.routers import service_router


# creating a router 
router = APIRouter()

# calling a router depends on prefix
router.include_router(service_router, prefix="/services", tags=["Services"]) 