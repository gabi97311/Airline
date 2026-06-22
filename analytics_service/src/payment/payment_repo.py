from sqlalchemy.ext.asyncio import AsyncSession

from .payment_models import AnalyticsPayment

class PaymenyRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
        