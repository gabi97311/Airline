from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.airplane_models import Airplane

import pandas as pd 

class AirplaneRepositories: 
    def __init__(self, session: Session):
        self.session = session
        
    def get_airplane_by_id(self, airplane_id: int) -> Airplane | None:
        return self.session.get(Airplane,airplane_id)
    
    def get_by_name(self, model: str) -> Airplane | None: 
        airplane = select(Airplane).where(Airplane.model_name == model)
        return self.session.execute(airplane).scalar()
    
    def get_airline_list(self) -> list[Airplane] | None:
        stmt = select(Airplane)
        result = self.session.execute(stmt)
        return result.scalars()
        
    def create_airplane(self, airplane: Airplane):
        try:
            self.session.add(airplane)
            self.session.commit()
            return airplane
        except Exception as e:
            self.session.rollback()
            raise e