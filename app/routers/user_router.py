from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemes.user_schemes import UserResponse
from app.schemes import AuthLogin
from app.jwt import decode_jwt

from app.repositories.users_repositories import UsersRepositories

http_bearer = HTTPBearer()

router = APIRouter(prefix='/users',tags=['users'])

def get_current_token_payload(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    token = credentials.credentials
    payload = decode_jwt(token=token)
    return payload

def get_current_auth_user(payload: dict = Depends(get_current_token_payload)) -> UserResponse:
    user_id: int = payload.get("sub")
    user = UsersRepositories.get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="User not found"
        )
        
    return user
    
    
def test_current_token_payload(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    if not credentials:
        raise HTTPException(status_code=404,detail='token broken')
    
    token = credentials.credentials
    print(f"\n\ntoken: {token}\n\n")
    payload = decode_jwt(token)
    
    return payload


@router.get('/me')
def get_user_info(user: UserResponse = Depends(get_current_auth_user) ):
    return user

@router.get('/test')
def check_problem(test_playload = Depends(test_current_token_payload)):
    return test_playload 
    
    