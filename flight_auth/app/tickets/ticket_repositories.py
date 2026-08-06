from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.tickets.ticket_model import Ticket as tk


class TicketRepositories:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_ticket(self, new_ticket: tk):
        self.session.add(new_ticket)
        await self.session.commit()
        await self.session.refresh(new_ticket)
        return new_ticket

    async def get_ticket_by_id(self, ticket_id: int) -> tk | None:
        return await self.session.get(tk, ticket_id)
    