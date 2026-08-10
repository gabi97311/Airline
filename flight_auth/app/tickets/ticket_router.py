from fastapi import APIRouter, Depends

from Airline.auth.src.users_model import UsersModel as User
from app.tickets.ticket_schemes import TicketCreate
from app.utils import Services, Jwt
from app.utils import Jwt
from app.utils.enums import TicketStatus
from app.tickets.broker import router as broker_router, ticket_exchange, ticket_queue_succeeded, ticket_queue_failed
router = APIRouter(prefix="/ticket", tags=["Ticket"])

@router.post("/purchase_ticket")
async def create_ticket(
    service: Services,
    ticket_details: TicketCreate = Depends(),
    user_id: User = Depends(Jwt.get_current_auth_user),
):
    return await service.ticket.create_ticket(ticket_details, user_id)

@router.get('/{ticket_id}')
async def get_ticket_by_id(
    service: Services, 
    ticket_id: int
): 
    return await service.ticket.get_ticket_by_id(ticket_id)

@router.post('/{ticket_id}/payment-details')
async def payment_date(ticket_id:int, user_id:int, service: Services):
    return await service.ticket.payment_date(ticket_id, user_id)

