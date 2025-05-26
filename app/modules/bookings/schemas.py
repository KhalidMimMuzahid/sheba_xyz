from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from modules.services.schemas import ServiceReferenceResponseForBookingService

class StatusTypeEnum(str, Enum):
    pending = "pending" #Booking request has been made but not yet confirmed.
    confirmed = "confirmed" # Booking is accepted and scheduled.
    in_progress= "in_progress" # The service is currently being provided.
    completed = "Completed" # The service has been successfully completed.
    cancelled="cancelled"   #Booking was cancelled by the user or provider.

class BookingCreateRequest(BaseModel):
    customer_name : str
    customer_phone: str
    service_id: int

class BookingCreateResponse(BaseModel):
    id: int
    customer_name : str
    customer_phone: str
    status: StatusTypeEnum
    service : ServiceReferenceResponseForBookingService
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True
        extra = "ignore"


class BookingListResponse(BookingCreateResponse):
    # extra_field: str  # Add extra fields if needed
    pass
