from decimal import Decimal
from sqlalchemy import Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.config_database.database import Base
from analytics_service.src.enums.analtics_enum import PaymentStatus

class AnalyticsPayment(Base):
    __tablename__ = 'analytics_payments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    flight_id: Mapped[int]
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus, name='payment_status')
    )
    payment_method: Mapped[str]