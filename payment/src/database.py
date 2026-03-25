from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Annotated
from fastapi import Depends

from src.config import settings

async_engine = create_async_engine(settings.DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(
    bind = async_engine,
    expire_on_commit= False
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
        
AsyncSessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass