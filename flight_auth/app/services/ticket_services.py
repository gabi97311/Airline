from fastapi import HTTPException,status

from app.models import UsersModel, Ticket
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

    async def create_ticket(self,ticket_details: TicketCreate, user: UsersModel):
        
        if not (flight :=self.flight_service.get_flight_by_id(ticket_details.flight_id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='flight not found')
        if not self.seat_service.get_seat_by_id(ticket_details.seat_id):
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='seat not found')
        new_ticket = Ticket(
            **ticket_details.model_dump(),
            user_id = user.id,
            flight_time = flight.flight_date
        )
        
        return self.ticket_repo.create_ticket(new_ticket)
        

        
