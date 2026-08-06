from fastapi import HTTPException

from airplane_models import Airplane
from app.airplanes.airplane_repositories import AirplaneRepositories
from app.airplanes.airplane_schemes import AirplaneOptions, AirplaneCreate, AirplaneResponse


class AirplaneServices:
    def __init__(self, airplane_repo: AirplaneRepositories):
        self.airplane_repo = airplane_repo
        
    async def create_airplane(self, airplane_details:AirplaneCreate) -> Airplane | None: 
        db_airplane = Airplane(**airplane_details.model_dump())
        
        if not await self.airplane_repo.create_airplane(db_airplane): 
            raise HTTPException(status_code=418, detail='Dias is teapot')
        
        return db_airplane
    
    async def get_airplane_by_id(self,airplane_id:int) -> Airplane:
        if not (airplane :=  await self.airplane_repo.get_airplane_by_id(airplane_id)): 
            raise HTTPException(status_code=404, detail='Airplane not found')
        return airplane
        
    async def get_airplane_list(self) -> list[AirplaneResponse]: 
        airplanes = await self.airplane_repo.get_airline_list()
        
        if not airplanes:
            raise HTTPException(status_code=404, detail='Airplanes not found')
        
        return airplanes
            
    async def get_airplane_options(self): 
        airplanes = await self.airplane_repo.get_airline_list()
        
        if not airplanes:
            raise HTTPException(status_code=404, detail='Airplanes not found')
        
        return [AirplaneOptions.model_validate(a) for a in airplanes]