from pydantic import BaseModel, Field


class AirplaneShemes(BaseModel): 
    
    model_name: str = Field(min_length=2, max_length=50, description='Airplane model')
    max_seats: int = Field(gt=0, description='Seats on Airplane')

class AirplaneResponse(AirplaneShemes):
    id: int