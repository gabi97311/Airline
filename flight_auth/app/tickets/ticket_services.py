from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import UsersModel, Ticket
from Airline.flight_auth.app.seats.seat_model import SeatStatus
from Airline.flight_auth.app.tickets.ticket_model import TicketStatus
from Airline.flight_auth.app.tickets.ticket_schemes import TicketCreate
from Airline.flight_auth.app.tickets.ticket_repositories import TicketRepositories

from app.services import FlightServices, SeatServices


class TicketServices:
    def __init__(
        self,
        session: AsyncSession, 
        ticket_repo: TicketRepositories,
        flight_service: FlightServices,
        seat_service: SeatServices,
    ):
        self.session = session
        self.ticket_repo = ticket_repo
        self.flight_service = flight_service
        self.seat_service = seat_service

    async def create_ticket(self, ticket_details: TicketCreate, user: UsersModel):

        flight = await self.flight_service.get_flight_by_id(ticket_details.flight_id)
        seat = await self.seat_service.reserve_seat(ticket_details.seat_id)

        new_ticket = Ticket(
            **ticket_details.model_dump(),
            user_id=user.id,
            flight_time=flight.flight_date,
            origin=flight.origin,
            dest=flight.dest,
            price=seat.price,
        )

        return await self.ticket_repo.create_ticket(new_ticket)

    async def get_ticket_by_id(self, ticket_id: int) -> Ticket:
        if not (ticket := await self.ticket_repo.get_ticket_by_id(ticket_id)):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found"
            )
        return ticket

    async def change_ticket_status(
        self, ticket_id: int, ticket_status: TicketStatus
    ) -> Ticket:
        ticket = await self.get_ticket_by_id(ticket_id)
        
        if ticket_status == TicketStatus.paid:
            await self.seat_service.update_seat_status(
                ticket.flight_id, ticket.seat_id, SeatStatus.occupied
            )
            ticket.ticket_status = TicketStatus.paid
        else:
            await self.seat_service.update_seat_status(
                ticket.flight_id, ticket.seat_id, SeatStatus.free
            )
            ticket.ticket_status = TicketStatus.failed 

        
        await self.session.commit()
        await self.ticket_repo.session.refresh(ticket) 
        return ticket

    async def payment_date(self, ticket_id: int, user_id: int) -> Ticket:
        ticket = await self.get_ticket_by_id(ticket_id)
        if ticket.ticket_status == TicketStatus.paid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="ticket was paid"
            )
        if ticket.user_id == user_id:
            return ticket
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="ticket another user"
            )
