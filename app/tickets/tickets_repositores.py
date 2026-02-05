from datetime import date
from app.tickets.tickets_schemes import TicketQuery
from sqlalchemy.orm import Session
from .tickets_model import TicketModel as ticket


class TicketRepositories:
    def __init__(self, session:Session): 
        self.session = session
    
    def create_ticket(self, ticket: ticket): 
        self.session.add(ticket)
        self.session.commit()
        
    def get_by_tickets(self, query:TicketQuery ):
        
        ticket_list = self.session.query(ticket)

        if query.flight_date is not None: 
           ticket_list = ticket_list.filter(ticket.flight_date == query.flight_date)
           
        if query.origin_state is not None:
            ticket_list = ticket_list.filter(ticket.origin_state == query.origin_state)
            
        if query.dest_state is not None:
            ticket_list = ticket_list.filter(ticket.dest_state == query.dest_state)
            
        if query.min_price is not None:
            ticket_list = ticket_list.filter(ticket.price > query.min_price)
            
        if query.max_price is not None:
            ticket_list = ticket_list.filter(ticket.price < query.max_price)
            
        if query.ticket_class is not None: 
            ticket_list = ticket_list.filter(ticket.ticket_class == query.ticket_class)
            
        if query.trip_type is not None: 
            ticket_list = ticket_list.filter(ticket.trip_type == query.trip_type)
        
        if query.sort_by is not None: 
            column = getattr(ticket, query.sort_by)
            if column: 
                if query.sort_order == 'desc':
                    ticket_list = ticket_list.order_by(column.desc())
                else:
                    ticket_list = ticket_list.order_by(column.asc())
                    
        offset_value = (query.page - 1) * query.size
        ticket_list = ticket_list.offset(offset_value).limit(query.size)
                    
        return ticket_list.all()
            
    def get_ticket_by_id(self, ticket_id: int): 
        return self.session.query(ticket).filter(ticket.ticket_id == ticket_id).first()
    