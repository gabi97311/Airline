from datetime import date

from sqlalchemy.orm import Session
from .tickets_model import TicketModel


class TicketRepositories:
    def __init__(self, session:Session): 
        self.session = session
    
    def create_ticket(self, ticket: TicketModel): 
        self.session.add(ticket)
        self.session.commit()
        
    def get_by_tickets(self) -> list[TicketModel]:
        return self.session.query(TicketModel).all()
            
    def get_ticket_by_id(self, ticket_id: int): 
        return self.session.query(TicketModel).filter(TicketModel.ticket_id == ticket_id).first()
    