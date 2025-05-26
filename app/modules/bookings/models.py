from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

# Define an enumeration for role type
class StatusTypeEnum(enum.Enum):
    pending = "pending" #Booking request has been made but not yet confirmed.
    confirmed = "confirmed" # Booking is accepted and scheduled.
    in_progress= "in_progress" # The service is currently being provided.
    completed = "Completed" # The service has been successfully completed.
    cancelled="cancelled"   #Booking was cancelled by the user or provider.



class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String,  unique=False, index=False)
    customer_phone = Column(String,  unique=False, index=False)
    service_id= Column(Integer, ForeignKey('services.id'), nullable=False)
    status = Column(Enum(StatusTypeEnum), nullable=False, default=StatusTypeEnum.pending)
    # relationship 
    service = relationship("Service", back_populates="bookings")

