from sqlalchemy.orm import Session 
from fastapi import HTTPException

from app.schemes.airplane_schemes import AirplaneCreate
from app.repositories.airplane_repositories import AirplaneRepositories
from app.models.airplane_models import Airplane


class AirplaneServices:
    def __init__(self, session: Session,airplane_repo: AirplaneRepositories ):
        self.session = session
        self.airplane_repo = airplane_repo
        
    def create_airplane(self, airplane_details:AirplaneCreate): 
        db_airplane = Airplane(**airplane_details.model_dump())
        
        if not self.airplane_repo.create_airplane(db_airplane): 
            raise HTTPException(status_code=418, detail='Dias is teapot')
        
        return db_airplane
        
    def get_airplane_list(self): 
        airplanes = self.airplane_repo.get_airline_list()
        
        if not airplanes:
            raise HTTPException(status_code=404, detail='Airplane not found')
            