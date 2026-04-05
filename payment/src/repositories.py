import httpx
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.payment_enum import PaymentStatus
from .models import PaymentModel


class PaymentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_purchase_intent(self, payment: PaymentModel) -> PaymentModel:
        self.session.add(payment)
        await self.session.commit()
        await self.session.refresh(payment)
        return payment

    async def update_payment_status(self, payment_id: int, payment_status: PaymentStatus):
        stmt = (
            update(PaymentModel)
            .where(PaymentModel.id == payment_id)
            .values(status= payment_status)
            .returning(PaymentModel)
        )
        result = await self.session.execute(stmt)
        if result.scalar_one_or_none(): 
            await self.session.commit()
        return result.scalar_one_or_none()

    async def get_payments(self):
        stmt = select(PaymentModel)
        result = await self.session.execute(stmt)
        return result.scalars()
