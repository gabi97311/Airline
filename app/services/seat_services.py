from sqlalchemy.orm import Session
from app.repositories.seat_repositories import SeatRepositories
class SeatServices:
    def __init__(self,session: Session, seat_repo: SeatRepositories):
        self.session = session
        self.seat_repo = seat_repo