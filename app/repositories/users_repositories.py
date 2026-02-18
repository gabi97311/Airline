from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.users_model import UsersModel

class UsersRepositories:
    def __init__(self, session: Session):
        self.session = session
        
    def add(self, user: UsersModel) -> None: 
        self.session.add(user)
        self.session.commit()
        
    def get_by_username(self,user_name: str) -> UsersModel | None:
        return( self.session.query(UsersModel).filter(UsersModel.user_name == user_name).first()) 
    
    def get_by_username(self, user_name: str) -> UsersModel | None: 
        stmt = select(UsersModel).where(UsersModel.user_name == user_name) 
        result = self.session.execute(stmt)
        return result.scalar()
    
    def get_user_by_id(self, user_id: int) -> UsersModel | None: 
        return (self.session.query(UsersModel).filter(UsersModel.id == user_id).first()) 
        