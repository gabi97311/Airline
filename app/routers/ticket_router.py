from fastapi import APIRouter, Depends
from app.schemes.flight_schemes import FlightQuery, FlightRevalidate
from app.schemes.user_schemes import UserResponse
from app.depends import TicketServiceDep
from app.depends import get_current_auth_user

router = APIRouter(prefix='/ticket', tags=['Ticket'])

@router.get('/list')
def get_flight_list(ticket_services: TicketServiceDep, query: FlightQuery = Depends()):
    return ticket_services.get_flight_list(query)

@router.get('/seats')
def get_seat_list(ticket_services: TicketServiceDep, flight_id: int):
    return ticket_services.get_seat_list

@router.get('/Purshase ticket')
def purchase_ticket(ticket_services: TicketServiceDep, seat_id: int, user:UserResponse = Depends(get_current_auth_user)):
    return ticket_services
