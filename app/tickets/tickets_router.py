from fastapi import APIRouter
from ..database import SessionDep
from .tickets_schemes import TicketQuery, CreateTicket, TicketResponse
from .tickets_repositores import TicketRepositories
from .ticket_service import TicketServices

def get_ticket_service(session: SessionDep) -> TicketServices:
    ticket_repo = TicketRepositories(session)
    return TicketServices(ticket_repo)

router = APIRouter(prefix='/tickets', tags=['Tickets'])


@router.post('/add_tickets')
def create_tickets(ticket: CreateTicket,):
    pass

@router.get('/get_tickets', response_model=TicketResponse)
def get_tickets(ticket: TicketQuery, ):
    pass

@router.get('tickets/{ticket_id}', response_model=TicketResponse)
def get_ticket_by_id(ticked_id: int):
    pass 

@router.get("/tickets/options")
def get_ticket_options():
    pass

@router.put("/tickets/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int):
    pass 

@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    pass