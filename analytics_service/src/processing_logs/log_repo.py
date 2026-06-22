from sqlalchemy.ext.asyncio import AsyncSession 

from .log_models import ProcessedEventsModel as pem

class ProcessedEventRepo:
    def _init__(self, session: AsyncSession):
        self.session = session
        
    