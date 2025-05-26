from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from exceptions.models import CustomError
from modules.services.models import Service
from modules.bookings.models import Booking
from modules.services.schemas import ServiceReferenceResponseForBookingService




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
    }