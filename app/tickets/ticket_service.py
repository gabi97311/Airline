from .tickets_repositores import TicketRepositories
from .tickets_schemes import TicketQuery, TicketResponse

class TicketServices:
    def __init__(self, ticket_repo: TicketRepositories):
        self.ticket_repo = ticket_repo
        
    def search_tickets(self, query:TicketQuery):
        ticket_list = self.ticket_repo.get_by_tickets(query)
        print(ticket_list)
        return ticket_list 
    
    
        