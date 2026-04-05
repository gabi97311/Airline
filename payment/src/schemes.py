from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

from src.payment_enum import PaymentStatus

class PaymentSchemes(BaseModel): 
    ticket_id: int
    user_id: int
    seat_id:int 
    flight_id: int
    amount: Decimal = Field(max_digits=10, decimal_places=2)
    status: PaymentStatus
    payment_method: str
    
class PaymentCreate(BaseModel):
    ticket_id: int 

class PaymentResponse(PaymentSchemes): 
    id: int 
    
