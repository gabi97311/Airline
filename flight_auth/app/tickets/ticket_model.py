from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func, Enum
from datetime import datetime
from typing import TYPE_CHECKING
import enum

from app.core import Base

if TYPE_CHECKING:
    from app.flights import Flight
    from app.seats import Seat


class TicketStatus(str, enum.Enum):
    paid = "paid"
    pending = "pending"
    failed = "failed"


class Ticket(Base):

    __tablename__ = "tickets"

    ticket_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    ticket_status: Mapped[TicketStatus] = mapped_column(
        Enum(TicketStatus, name="ticket_status"),
        default=TicketStatus.pending,
        server_default=TicketStatus.paid.value,
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.seat_id"))
    seat: Mapped["Seat"] = relationship(back_populates="ticket")

    flight_id: Mapped[int] = mapped_column(ForeignKey("flights.flight_id"))
    flight: Mapped["Flight"] = relationship(back_populates="tickets")

    origin: Mapped[str]
    dest: Mapped[str]

    passenger_name: Mapped[str]

    purchase_time: Mapped[datetime] = mapped_column(server_default=func.now())

    flight_time: Mapped[datetime]

    price: Mapped[float]
