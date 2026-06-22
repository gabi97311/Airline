from .log_repo import ProcessedEventReop as per

class ProcessedEventService:
    def __init__(self, repo: per):
        self.repo = repo
        
    async def get_event_by_id(self, event_id: int):
        pass