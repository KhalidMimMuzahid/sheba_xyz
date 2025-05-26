from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String,  unique=True, index=False)
    customer_phone = Column(String,  unique=False, index=False)
    service_id= Column(Integer, ForeignKey('services.id'), nullable=False)
    status = Column(String,  unique=False, index=False)
    # relationship 
    service = relationship("Service", back_populates="bookings")

