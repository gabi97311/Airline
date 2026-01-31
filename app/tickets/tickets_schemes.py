from pydantic import BaseModel
from fastapi import Query
from typing import Literal, Optional
from datetime import date



class TicketSchemes(BaseModel):
    
    flight_date: date
    origin: str
    origin_state: str 
    dest: str 
    dest_state: str
    crs_dep_time: int
    ticket_class: Literal['economy','comfort','business','first_class']
    trip_type: Literal['one-way','round-trip']
    price: float

class CreateTicket(TicketSchemes):
    pass

class TicketResponse(TicketSchemes):
    id: int


class TicketQuery(BaseModel):
    
    flight_date: Optional[date]
    origin_state: Optional[str]
    dest_state: Optional[str]
    min_price: Optional[float]
    max_price: Optional[float]
    ticket_class: Optional[Literal['economy','comfort','business','first_class']]
    trip_type: Optional[Literal['one-way','round-trip']]
    sort_by: Optional[Literal['price', 'flight_date']] = 'price'
    sort_order: Optional[Literal['asc', 'desc']] = 'asc'
