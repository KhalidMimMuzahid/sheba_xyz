from pydantic import BaseModel

class ServiceCreateRequest(BaseModel):
    name : str
    category : str
    description : str
    price : int

class ServiceCreateResponse(BaseModel):
    id: int
    name : str
    category : str
    description : str
    price : int
    class Config:
        orm_mode = True
        extra = "ignore"

class ServiceListResponse(ServiceCreateResponse):
    # extra_field: str  # Add extra fields if needed
    pass

class ServiceReferenceResponseForBookingService(BaseModel):
    id: int
    name : str
    category : str
    # description : str
    # price : int
    class Config:
        orm_mode = True
        extra = "ignore"
