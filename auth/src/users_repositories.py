from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from Airline.auth.src.users_model import UsersModel

class UsersRepositories:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def add(self, user: UsersModel) -> None: 
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        
    async def get_by_username(self,user_name: str) -> UsersModel | None:
        stmt = select(UsersModel).where(UsersModel.user_name == user_name)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def get_user_by_id(self, user_id: int) -> UsersModel | None: 
        return await self.session.get(UsersModel, user_id)
        