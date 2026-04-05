from fastapi import APIRouter, Depends

from app.models.users_model import UsersModel as User
from app.schemes.ticket_schemes import TicketCreate
from app.depends import TicketServiceDep
from app.depends import get_current_auth_user

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