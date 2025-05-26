
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db 
from responses.models import Response
from responses.handler import create_response
from modules.bookings.services import booking_service, get_bookings, check_booking_status_service
from modules.bookings.schemas import BookingCreateRequest, BookingCreateResponse, BookingListResponse, checkBookingStatusResponse


booking_router = APIRouter()

@booking_router.post("/booking-service", response_model=  Response[BookingCreateResponse])
async def add_service(booking: BookingCreateRequest, db: AsyncSession = Depends(get_db)):
    result= await booking_service(db=db, customer_name= booking.customer_name, customer_phone= booking.customer_phone, customer_email= booking.customer_email, service_id=booking.service_id )
    return create_response(result=result, pydantic_model=BookingCreateResponse, message="Service has booked successfully")

@booking_router.get("/get-bookings"
, response_model=Response[list[BookingListResponse]]
)
async def list_services(db: AsyncSession = Depends(get_db), page:int=1, limit:int=10):
    result= await get_bookings(db, page, limit)
    return create_response(result=result["data"], pydantic_model=BookingListResponse, message="Bookings have retrieved successfully", meta_data=result["meta_data"] )
    
@booking_router.get("/check-booking-status"
, response_model=Response[checkBookingStatusResponse]
)
async def check_booking_status(db: AsyncSession = Depends(get_db), booking_id : int= None ):
    result= await check_booking_status_service(db,booking_id)
    return create_response(result=result, pydantic_model=checkBookingStatusResponse, message="Booking data has retrieved successfully" )
    