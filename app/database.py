import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
from sqlalchemy.orm import sessionmaker,Session
from typing import Annotated
from fastapi import Depends

engine = db.create_engine(
    settings.DATABASE_URL,
)

SessionLocal = sessionmaker(bind=engine)

def get_session():
    with SessionLocal() as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

class Base(DeclarativeBase):
    pass 

def create_table():
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

