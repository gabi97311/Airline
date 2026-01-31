from pydantic import BaseModel, Field
from typing import Optional
import enum


class UserRole(enum.Enum):
    user = 'user'
    admin = "admin"
    
class UserStatus(enum.Enum):
    online = 'online'
    offline = 'offline'

class UserCreate(BaseModel):
    user_name: str = Field(..., max_length=100)
    user_password: str 
    role: Optional[UserRole] = UserRole.user


class UserResponse(BaseModel):
    id: int
    user_name: str
    role: UserRole
    status: bool

    class Config:
        orm_mode = True
