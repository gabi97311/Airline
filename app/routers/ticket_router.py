from fastapi import APIRouter, Depends
from app.schemes.flight_ticket_schemes import FlightTicketQueary, FlightRevalidate
from app.depends import TicketServiceDep

router = APIRouter(prefix='/ticket', tags=['Ticket'])

@router.get('/list')
def get_flight_list(ticket_services: TicketServiceDep, query: FlightTicketQueary = Depends()):
    return ticket_services.get_flight_list(query)

