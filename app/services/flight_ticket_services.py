from app.models.flight_models import Flight
from app.repositories.flight_ticket_repositories import FlightTicketRepositories
from app.schemes.flight_ticket_schemes import FlightTicketQueary, FlightRevalidate
from app.exceptions.flight_exceptions import FlightErrors



class FlightTicketServices:
    def __init__(self, ticket_repo:FlightTicketRepositories): 
        self.ticket_repo = ticket_repo
        
    def get_flight_list(self, query: FlightTicketQueary):
        return self.ticket_repo.get_flight_list(query)
    
        