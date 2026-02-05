from pydantic import BaseModel, ConfigDict
from fastapi import Query
from typing import Literal, Optional
from datetime import date

from app.tickets.tickets_model import TicketClass, TripType



class TicketSchemes(BaseModel):
    flight_date: date
    origin: str
    origin_state: str 
    dest: str 
    dest_state: str
    crs_dep_time: int
    
    ticket_class: TicketClass 
    trip_type: TripType 
    
    price: float

    model_config = ConfigDict(
        from_attributes=True, 
        use_enum_values=True,
        
    )

class CreateTicket(TicketSchemes):
    pass

class TicketResponse(TicketSchemes):
    ticket_id: int


class TicketQuery(BaseModel):
    
    flight_date: Optional[date] = None 
    origin_state: Optional[str] = None 
    dest_state: Optional[str] = None 
    min_price: Optional[float] = None 
    max_price: Optional[float] = None 
    
    ticket_class: Optional[Literal['economy','comfort','business','first_class']] = None 
    trip_type: Optional[Literal['one_way','round_trip']] = None 
    sort_by: Optional[Literal['price', 'flight_date']] = 'price'
    sort_order: Optional[Literal['asc', 'desc']] = 'asc'
    page: int = 1
    size: int = 20
    

    
