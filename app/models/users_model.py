import enum

from typing import List, TYPE_CHECKING
from sqlalchemy import Enum, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.tickets.tickets_model import TicketModel

class UserRole(enum.Enum):
    
    user = 'user'
    admin = "admin"
    
class UserStatus(enum.Enum):
    online = 'online'
    offline = 'offline'

class UsersModel(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    user_password: Mapped[bytes] = mapped_column( LargeBinary, nullable=False )
    salt: Mapped[bytes] = mapped_column( LargeBinary, nullable=False)
    # tickets = Mapped[List] = mapped_column
    role: Mapped[UserRole] = mapped_column( Enum(UserRole, name="user_role"), default=UserRole.user, server_default="user" )
    status: Mapped[bool] = mapped_column(default=False)