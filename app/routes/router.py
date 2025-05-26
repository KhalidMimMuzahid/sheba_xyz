from fastapi import APIRouter
from modules.services.routers import service_router
from modules.bookings.routers import booking_router


# creating a router 
router = APIRouter()

# calling a router depends on prefix
router.include_router(service_router, prefix="/services", tags=["Services"]) 
router.include_router(booking_router, prefix="/booking", tags=["Bookings"]) 