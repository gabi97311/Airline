from fastapi import APIRouter,Depends
from app.schemes.user_schemes import UserResponse
from app.depends import get_current_auth_user

router = APIRouter(prefix='/users',tags=['users'])

@router.get('/me', response_model=UserResponse)
async def get_user_info(user: UserResponse = Depends(get_current_auth_user)):
    return user


    
    