from app.repositories.users_repositories import UsersRepositories
from fastapi import HTTPException, status

AuthenticationException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
)

class UserServices:
    
    def __init__(self, user_repo: UsersRepositories):
        self.user_repo = user_repo
        
    async def get_user_info(self, user_id: int):
        user = await self.user_repo.get_user_by_id(user_id)
        
        if not user:
            raise AuthenticationException
        
        return user
        