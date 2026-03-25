from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

from src.payment_enum import PaymentStatus

class PaymentSchemes(BaseModel): 
    flight_id: int
    seat_id:int 
    user_id:int
    amount: Decimal = Field(max_digits=10, decimal_places=2)
    
    class Config:
        coerce_numbers_to_str = False
        
class PaymentCreate(PaymentSchemes):
    pass 

class PaymentResponse(PaymentSchemes): 
    id: int 
    status: PaymentStatus
    payment_method: str
    model_config = ConfigDict(from_attributes=True)