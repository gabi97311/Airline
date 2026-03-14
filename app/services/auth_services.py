from fastapi import HTTPException

from app.schemes import TokenInfo
from app.models.users_model import UsersModel
from app.hashing import getHash, get_hash_to_auth
from app.repositories import UsersRepositories
from app.jwt import encode_jwt




class AuthServices: 
    
    def __init__(self, user_repo: UsersRepositories):
        self.user_repo = user_repo
        
    async def register(self, user_name:str, user_password:str ) -> UsersModel:
        if await self.user_repo.get_by_username(user_name):
            raise HTTPException(status_code=409, detail='User already exists')
        
        salt, hash_password = getHash(user_password)
        
        user = UsersModel(
            user_name = user_name,
            user_password = hash_password,
            salt = salt 
        )
        await self.user_repo.add(user)
        return {'message':"User created successfully"}
    
    
    async def login(self, user_name:str, user_password:str) -> TokenInfo: 
        if not(user := await self.user_repo.get_by_username(user_name)):
            raise HTTPException(status_code=401, detail='invalid username or password')
    
        password = get_hash_to_auth(user.salt, user_password)
        
        if user.user_password != password:
            raise HTTPException(status_code=401, detail='invalid username or password')
        
        jwt_playload = {
            'sub': str(user.id),
            'user_name' : user.user_name,
            'role' : user.role.value,
        }
        token = encode_jwt(jwt_playload)
        
        return TokenInfo(access_token=token,token_info='bearer')
        