import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.config_database.database import Base
from src.analtics_enum import SeatClass, SeatStatus

class AnalyticsSeat(Base):
    __tablename__ = 'analytics_seats'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    flight_id: Mapped[int]
    seat_class: Mapped[SeatClass] = mapped_column(
        Enum(SeatClass, name='seat_class', values_callable=lambda obj: [e.value for e in obj])
    )
    seat_status: Mapped[SeatStatus] = mapped_column(
        Enum(SeatStatus, name='seat_status', values_callable=lambda obj: [e.value for e in obj])
    )
    price: Mapped[float]