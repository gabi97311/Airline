from fastapi import APIRouter, Depends

from app.models.users_model import UsersModel as User
from app.schemes.ticket_schemes import TicketCreate
from app.depends import TicketServiceDep
from app.depends import get_current_auth_user
from app.models.ticket_model import TicketStatus

router = APIRouter(prefix="/ticket", tags=["Ticket"])

@router.post("/create_ticket")
async def create_ticket(
    ticket_service: TicketServiceDep,
    ticket_details: TicketCreate = Depends(),
    user: User = Depends(get_current_auth_user),
):
    return await ticket_service.create_ticket(ticket_details, user)

@router.get('/{ticket_id}')
async def get_ticket_by_id(
    ticket_service: TicketServiceDep, 
    ticket_id: int
): 
    return await ticket_service.get_ticket_by_id(ticket_id)


# router for payment_micro service

@router.post('/{ticket_id}/payment-details')
async def payment_date(ticket_id:int, user_id:int, ticket_service: TicketServiceDep):
    return await ticket_service.payment_date(ticket_id, user_id)

@router.post('/{ticket_id}/confirm')
async def confirm_ticket_payment(ticket_id:int, ticket_service: TicketServiceDep):
    return await ticket_service.change_ticket_status(ticket_id, TicketStatus.paid)

@router.post('/{ticket_id}/cancel')
async def cancel_ticket_payment(ticket_id:int, ticket_service: TicketServiceDep): 
    return await ticket_service.change_ticket_status(ticket_id, TicketStatus.failed)