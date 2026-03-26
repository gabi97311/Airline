from app.repositories.ticket_repositories import TicketRepositories

class TicketServices:
    def __init__ (self, ticket_repo: TicketRepositories):
        self.ticket_repo = ticket_repo