from fastapi import APIRouter
from app.modules.services.routers import service_router
from app.modules.bookings.routers import booking_router
from app.modules.users.routers import user_router


# creating a router 
router = APIRouter()

# calling a router depends on prefix
router.include_router(user_router, prefix="/users", tags=["Users"]) 
router.include_router(service_router, prefix="/services", tags=["Services"]) 
router.include_router(booking_router, prefix="/bookings", tags=["Bookings"]) 