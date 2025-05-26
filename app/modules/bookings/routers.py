
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db 
from responses.models import Response
from responses.handler import create_response
from modules.bookings.services import booking_service, get_bookings
from modules.bookings.schemas import BookingCreateRequest, BookingCreateResponse, BookingListResponse


booking_router = APIRouter()

@booking_router.post("/booking-service", response_model=  Response[BookingCreateResponse])
async def add_service(booking: BookingCreateRequest, db: AsyncSession = Depends(get_db)):
    result= await booking_service(db=db, customer_name= booking.customer_name, customer_phone= booking.customer_phone, service_id=booking.service_id )
    return create_response(result=result, pydantic_model=BookingCreateResponse, message="Service has booked successfully")

@booking_router.get("/get-bookings"
, response_model=Response[list[BookingListResponse]]
)
async def list_services(db: AsyncSession = Depends(get_db), page:int=1, limit:int=10):
    result= await get_bookings(db, page, limit)
    # return result
    return create_response(result=result["data"], pydantic_model=BookingListResponse, message="Bookings have retrieved successfully", meta_data=result["meta_data"] )
    