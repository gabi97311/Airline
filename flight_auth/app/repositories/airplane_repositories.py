from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.models.airplane_models import Airplane

class AirplaneRepositories: 
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_airplane_by_id(self, airplane_id: int) -> Airplane | None:
        return await self.session.get(Airplane,airplane_id)
    
    async def get_by_name(self, model: str) -> Airplane | None: 
        airplane = select(Airplane).where(Airplane.model_name == model)
        result = await self.session.execute(airplane)
        return result.scalar_one()
    
    async def get_airline_list(self) -> list[Airplane] | None:
        stmt = select(Airplane)
        result = await self.session.execute(stmt)
        return result.scalars().all()
        
    async def create_airplane(self, airplane: Airplane):
        try:
            self.session.add(airplane)
            await self.session.commit()
            await self.session.refresh(airplane)
            return airplane
        except Exception as e:
            await self.session.rollback()
            raise e