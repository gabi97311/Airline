from pydantic import BaseModel,Field

class RegisterSchemes(BaseModel):
    user_name: str = Field(..., max_length=100)
    user_password: str = Field(...)
    
class AuthLogin(BaseModel):
    user_name: str = Field(..., max_length=100)
    user_password: str = Field(...)