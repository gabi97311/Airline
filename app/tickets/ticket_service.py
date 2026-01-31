from .tickets_repositores import TicketRepositories
from .tickets_schemes import TicketQuery

class TicketServices:
    def __init__(self, ticket_repo: TicketRepositories):
        self.ticket_repo = ticket_repo
        
    def get_ticket(self,query: TicketQuery ):
        pass
        