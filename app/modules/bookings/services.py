from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from exceptions.models import CustomError
from modules.services.models import Service
from modules.bookings.models import Booking
from modules.services.schemas import ServiceReferenceResponseForBookingService
from utils.query_builder import query_builder
from modules.bookings.utils import transform_service_data



async def booking_service(db: AsyncSession, customer_name: str, customer_phone:str ,service_id = int):
     # checking for existence service with the provided service_id
    service_result = await db.execute(select(Service).where(Service.id == service_id))
    service = service_result.scalar_one_or_none()
    if not service:
     raise CustomError(message= "No service found with this id", status_code=404, resolution="please provide valid service_id")
     #  making an instance of the booking object that inherits from Booking Class (Models class)
    new_booking = Booking(customer_name=customer_name, customer_phone=customer_phone, service_id= service.id)
    db.add(new_booking)
    await db.commit()
    await db.refresh(new_booking)

    return {
          "id" : new_booking.id,
          "customer_name" :new_booking.customer_name,
          "customer_phone" : new_booking.customer_phone,
          "status": new_booking.status,
          "service":  ServiceReferenceResponseForBookingService(**new_booking.service.__dict__),
          "created_at" : new_booking.created_at,
          "updated_at" : new_booking.updated_at
    }



async def get_bookings(db: AsyncSession, page:int, limit:int):
    return await query_builder(
        db=db,
        model=Booking,
        page=page,
        limit=limit,
        relationships=[Booking.service],  #  Joined load applied
        transform_fn=transform_service_data  #  Transform function applied
    )


async def check_booking_status_service(db: AsyncSession, booking_id = int):
    booking_result = await db.execute(select(Booking).where(Booking.id == booking_id).options(joinedload(Booking.service)))
    booking = booking_result.scalar_one_or_none()
    if not booking:
     raise CustomError(message= "No booking found with this id", status_code=404, resolution="please provide valid booking_id")
     #  making an instance of the booking object that inherits from Booking Class (Models class)


    return {
          "id" : booking.id,
          "customer_name" :booking.customer_name,
          "customer_phone" : booking.customer_phone,
          "status": booking.status,
          "service":  ServiceReferenceResponseForBookingService(**booking.service.__dict__),
          "created_at" : booking.created_at,
          "updated_at" : booking.updated_at
    }