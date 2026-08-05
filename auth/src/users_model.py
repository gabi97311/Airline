import enum

from typing import List, TYPE_CHECKING
from sqlalchemy import Enum, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING: 
    from app.models.ticket_model import Ticket


class UserRole(enum.Enum):
    user = 'user'
    admin = "admin"

class UsersModel(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    user_password: Mapped[bytes] = mapped_column( LargeBinary, nullable=False )
    salt: Mapped[bytes] = mapped_column( LargeBinary, nullable=False)
    role: Mapped[UserRole] = mapped_column( Enum(UserRole, name="user_role"), default=UserRole.user, server_default="user")
    status: Mapped[bool] = mapped_column(default=True)
    
    tickets: Mapped[List['Ticket']] = relationship(back_populates='user')