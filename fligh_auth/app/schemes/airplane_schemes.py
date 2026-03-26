from pydantic import BaseModel, ConfigDict, Field


class AirplaneShemes(BaseModel): 
    
    model_name: str = Field(min_length=2, max_length=50, description='Airplane model')
    max_seats: int = Field(gt=0, description='Seats on Airplane')
    
    model_config = ConfigDict(from_attributes=True)

class AirplaneCreate(AirplaneShemes):
    pass

class AirplaneResponse(AirplaneShemes):
    airplane_id: int
    
class AirplaneOptions(BaseModel):
    airplane_id: int
    model_name: str
    
    class Config:
        from_attributes = True