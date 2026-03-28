from fastapi import HTTPException, status

from app.models import UsersModel, Ticket
from app.models.seat_model import SeatStatus
from app.schemes.ticket_schemes import TicketCreate
from app.repositories.ticket_repositories import TicketRepositories

from app.services import FlightServices, SeatServices


class TicketServices:
    def __init__(
        self,
        ticket_repo: TicketRepositories,
        flight_service: FlightServices,
        seat_service: SeatServices,
    ):
        self.ticket_repo = ticket_repo
        self.flight_service = flight_service
        self.seat_service = seat_service

    async def create_ticket(self, ticket_details: TicketCreate, user: UsersModel):
        print(f"\n\n\n\n\n\n\nUser id: {user.id} \n\n\n\n\n\n\n")

        flight = await self.flight_service.get_flight_by_id(ticket_details.flight_id)
        seat = await self.seat_service.reserve_seat(ticket_details.seat_id)

        new_ticket = Ticket(
            **ticket_details.model_dump(),
            user_id = user.id,
            flight_time = flight.flight_date
            )

        return await self.ticket_repo.create_ticket(new_ticket)
