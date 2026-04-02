import httpx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import PaymentModel

class PaymentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def create_purchase_intent(self, payment: PaymentModel):
        self.session.add(payment)
        await self.session.commit()
        return payment
        
    async def update_payment_status(self, status: str): 
        pass
    
    async def get_payments(self):
        stmt = select(PaymentModel)
        result = await self.session.execute(stmt)
        return result.scalars()
    