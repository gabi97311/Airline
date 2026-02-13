from pydantic import BaseModel
from datetime import date 

class FlightTicketSchemes(BaseModel):
    
    flight_date: date
    reporting_airline: str
    origin: str
    dest: str
    plane_model: str
    is_delay: bool 


class FlightTicketCreate(BaseModel):
    pass

class FlightTicketResponse(BaseModel): 
    flight_id: int 
    reporting_airline: str
    origin: str
    dest: str
    plane_model: str
    is_delay: bool 
    
class FlightTicketQueary(BaseModel):
    pass 