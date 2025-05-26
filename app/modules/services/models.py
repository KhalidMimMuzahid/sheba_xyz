from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  unique=False, index=False)
    category = Column(String,  unique=False, index=False)
    description = Column(String,  unique=False, index=False)
    price = Column(Integer,  unique=False, index=False)
    

    
    # Reverse relationship
    bookings = relationship("Booking", back_populates="service", cascade="all, delete")




