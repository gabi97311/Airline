from typing import Annotated
from fastapi import Depends

from app.database import SessionDep
from app.tickets.tickets_repositores import TicketRepositories
from app.tickets.ticket_service import TicketServices



def get_ticket_service(session: SessionDep) -> TicketServices:
    return TicketServices(TicketRepositories(session))

TicketServiceDep = Annotated[TicketServices,Depends(get_ticket_service)]