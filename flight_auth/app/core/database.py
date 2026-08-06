from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from .config import settings


engine = create_async_engine(settings.AUTH_DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    expire_on_commit=False 
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

AsyncSessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass 

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
