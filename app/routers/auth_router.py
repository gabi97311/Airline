from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer

from app.database import SessionDep
from app.schemes import RegisterSchemes
from app.services import AuthServices
from app.repositories import UsersRepositories
from app.jwt import decode_jwt

router = APIRouter(prefix='/auth', tags=['Auth'])

def get_auth_service(session: SessionDep) -> AuthServices:
    user_repo = UsersRepositories(session)
    return AuthServices(user_repo)

@router.post('/register')
def register_new_user(user: RegisterSchemes, auth_service: AuthServices = Depends(get_auth_service)):
    return (auth_service.register(
        user.user_name,
        user.user_password
    ))

@router.post('/login')
def login(
    user_name: str = Form(...),
    user_password: str = Form(...),
    auth_service: AuthServices = Depends(get_auth_service)
):
    return auth_service.login(
        user_name,
        user_password
    )




