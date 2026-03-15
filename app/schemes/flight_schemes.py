from typing import Literal, Optional
from pydantic import BaseModel,Field
from datetime import date 

class FlightTicketSchemes(BaseModel):
    
    flight_date: date
    reporting_airline: str
    origin: str
    dest: str
    airplane_id: int
    is_delay: bool = False


class FlightCreate(FlightTicketSchemes):
    pass

class FlightResponse(BaseModel): 
    flight_id: int 
    reporting_airline: str
    origin: str
    dest: str
    plane_model: str
    is_delay: bool 

class FlightRevalidate(BaseModel): 
    flight_id: int 
    price: float
    
class FlightQuery(BaseModel):
    flight_date: Optional[date]
    origin: Optional[str]
    dest: Optional[str]
    min_price: Optional[float]
    max_price: Optional[float]
    ticket_class: Optional[Literal['economy','comfort','business','first_class']]
    sort_by: Optional[Literal['price', 'flight_date']] = 'price'
    sort_order: Optional[Literal['asc', 'desc']] = 'asc'
    page: int = Field(default=1, ge=1)
    size: int = Field(default=20, ge=1, le=100)