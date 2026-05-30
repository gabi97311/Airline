from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Annotated
from fastapi import Depends

from .config import settings

async_engine = create_async_engine(settings.ANALYTICS_DATABASE_URL)
flight_async_engine = create_async_engine(settings.AUTH_DATABASE_URL)
pay_async_engine = create_async_engine(settings.PAY_DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(
    bind = async_engine,
    expire_on_commit= False
)

FlightAsyncSessionLocal = async_sessionmaker(
    bind = flight_async_engine,
    expire_on_commit= False
)

PayAsyncSessionLocal = async_sessionmaker(
    bind= pay_async_engine,
    expire_on_commit=False
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

async def get_flight_session():
    async with FlightAsyncSessionLocal() as session:
        yield session

async def get_pay_session():
    async with PayAsyncSessionLocal() as session:
        yield session
        
AsyncSessionDep = Annotated[AsyncSession, Depends(get_session)]
FlightSessionDep = Annotated[AsyncSession, Depends(get_flight_session)]
PaySessionDep = Annotated[AsyncSession, Depends(get_pay_session)]

class Base(DeclarativeBase):
    pass