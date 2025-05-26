from typing import Any, Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class MetaData(BaseModel):
    previous_page: Optional[int]  # Can be int or None
    next_page: Optional[int]  # Can be int or None
    current_page: int
    total_page: int # total number of pages depending on page limit
    class Config:
        orm_mode = True


class Response(BaseModel, Generic[T]):
    is_success: bool = True
    message: str
    data: T
    meta_data: Optional[MetaData]
