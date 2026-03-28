import httpx
from fastapi import Depends

from src.repositories import PaymentRepository
from src.schemes import PaymentCreate

class PaymentService: 
    def __init__ (self, repo: PaymentRepository):
        self.repo = repo
        
    async def create_purchase_intent(self, payment_details: PaymentCreate, user_id:int):
        
    async def get_payment(self):
        pass