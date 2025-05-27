from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from exceptions.models import CustomError
from modules.services.models import Service
from modules.bookings.models import Booking
from modules.services.schemas import ServiceReferenceResponseForBookingService
from utils.query_builder import query_builder
from modules.bookings.utils import transform_service_data
from utils.send_mail import send_email, EmailSchema
from modules.bookings.utils import make_html_body, make_html_body_for_changing_status
from modules.bookings.schemas import StatusTypeEnum

async def booking_service(db: AsyncSession, customer_name: str, customer_phone:str, customer_email:str, service_id = int):
     # checking for existence service with the provided service_id
    service_result = await db.execute(select(Service).where(Service.id == service_id))
    service = service_result.scalar_one_or_none()
    if not service:
     raise CustomError(message= "No service found with this id", status_code=404, resolution="please provide valid service_id")
     #  making an instance of the booking object that inherits from Booking Class (Models class)
    new_booking = Booking(customer_name=customer_name, customer_phone=customer_phone, customer_email=customer_email, service_id= service.id)
    db.add(new_booking)
    await db.commit()
    await db.refresh(new_booking)

    # sending mail to the user
    is_sent=await send_email(EmailSchema(
        receiver_email=customer_email,
        subject="Your Service has booked successfully",
        html_body = make_html_body(customer_name, customer_phone, customer_email, service_id)
    )) 
    # print("email has sent successfully" if is_sent else "email has not sent somehow")

    return {
          "id" : new_booking.id,
          "customer_name" :new_booking.customer_name,
          "customer_phone" : new_booking.customer_phone,
          "customer_email": new_booking.customer_email,
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
          "customer_email": booking.customer_email,
          "status": booking.status,
          "service":  ServiceReferenceResponseForBookingService(**booking.service.__dict__),
          "created_at" : booking.created_at,
          "updated_at" : booking.updated_at
    }

async def update_booking_status(
    db: AsyncSession,
    booking_id: int,
    status: StatusTypeEnum,
):
    booking_result = await db.execute(select(Booking).where(Booking.id == booking_id).options(joinedload(Booking.service)))
    booking = booking_result.scalar_one_or_none()
    if not booking:
     raise CustomError(message= "No booking found with this id", status_code=404, resolution="please provide valid booking_id")

    # Update Booking data
    if status:
        booking.status= status
    await db.commit()
    await db.refresh(booking)
        # sending mail to the user
    is_sent=await send_email(EmailSchema(
        receiver_email=booking.customer_email,
        subject=f"Your Booking status has changed to {booking.status.value}",
        html_body = make_html_body_for_changing_status(customer_name= booking.customer_name, customer_phone=booking.customer_phone, customer_email=booking.customer_email, booking_id=booking.id, status=booking.status.value)
    )) 
    # print("email has sent successfully" if is_sent else "email has not sent somehow")

    return {
          "id" : booking.id,
          "customer_name" :booking.customer_name,
          "customer_phone" : booking.customer_phone,
          "customer_email": booking.customer_email,
          "status": booking.status.value,
          "service":  ServiceReferenceResponseForBookingService(**booking.service.__dict__),
          "created_at" : booking.created_at,
          "updated_at" : booking.updated_at
    }