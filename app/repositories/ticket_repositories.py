from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.ticket_model import Ticket as tk

class TicketRepositories:
    def __init__(self,session: Session):
        self.session = session
        
    def get_ticket_list(self, flight_id: int) -> tk:
        stmt = select(tk).where(tk.flight_id == flight_id)
        result = self.session.execute(stmt)
        return result.scalars().all()
    
    def get_ticket_by_id(self, ticket_id:int) -> list[tk]:
        return self.session.get(tk,ticket_id)
    
    def create_ticket(self, user_id: int, seat_id: int):
        pass 