from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, Enum

from database import Base
from payment_enum import PaymentStatus

class PaymentModel(Base): 
    id: Mapped[int] = mapped_column(primary_key=True)
    flight_id: Mapped[int] = mapped_column(nullable=False)
    seat_id: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False) 
    amount: Mapped[Decimal] = mapped_column(Numeric(10,2))
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus, name = 'payment_status'), default= PaymentStatus.pending, server_default=PaymentStatus.pending.value)
    payment_method: Mapped[str]
    