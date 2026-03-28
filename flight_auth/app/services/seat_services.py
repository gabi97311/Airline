from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


import numpy as np

from app.models.seat_model import Seat
from app.models.airplane_models import Airplane
from app.schemes.seat_schemes import SeatClass, SeatStatus

from app.repositories.seat_repositories import SeatRepositories


class SeatServices:

    def __init__(self, session: AsyncSession, seat_repo: SeatRepositories):
        self.session = session
        self.seat_repo = seat_repo

    async def get_seat_list(self, flight_id: int):
        seats = await self.seat_repo.get_seat_list(flight_id)
        return seats

    async def get_seat_by_id(self, seat_id: int):
        seat = await self.seat_repo.get_seat_by_id(seat_id)
        if not seat:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND, detail="There is no such place"
            )

    async def get_seat_by_id_with_for_update(self, seat_id: int) -> Seat:
        seat = await self.seat_repo.get_seat_for_update(seat_id)
        return seat

    async def reserve_seat(self, seat_id: int) -> Seat:
        if not (seat := await self.get_seat_by_id_with_for_update(seat_id)):
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Seat not found")
        if seat.seat_status != SeatStatus.free:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail="Seat is already occupied or reserved",
            )
        seat.seat_status = SeatStatus.pending
        return seat
    

    async def generate_seats_for_flight(self, flight_id: int, airplane: Airplane):
        seats_data_list = self._build_seat_dataframe(flight_id, airplane)
        try:
            seat = [Seat(**seat_dict) for seat_dict in seats_data_list]
            self.session.add_all(seat)
        except Exception as e:
            await self.session.rollback()
            raise e

    # func to genarate seat for flight
    def _build_seat_dataframe(self, flight_id: int, airplane: Airplane):
        max_seat = airplane.max_seats
        default_price = np.random.randint(45, 55)
        letters = ["A", "B", "C", "D", "E", "F"]
        seat_data = []
        seat_count = 0

        # seat_class - probability - multiplications
        seat_class = [
            (SeatClass.economy, 0.4, 1.0),
            (SeatClass.comfort, 0.3, 1.5),
            (SeatClass.business, 0.2, 3),
            (SeatClass.first, 0.1, 5),
        ]

        for s_class, shape, multiplier in seat_class:
            class_limit = int(max_seat * shape)
            for _ in range(class_limit):
                if seat_count > max_seat:
                    break

                row = (seat_count // len(letters)) + 1
                letter = seat_count % len(letters)

                seat_data.append(
                    {
                        "flight_id": flight_id,
                        "seat_code": f"{row}{letter}",
                        "seat_class": s_class,
                        "price": float(default_price * multiplier),
                        "seat_status": SeatStatus.free,
                    }
                )
                seat_count += 1

        while seat_count < max_seat:
            row = (seat_count // len(letters)) + 1
            letter = seat_count % len(letters)

            seat_data.append(
                {
                    "flight_id": flight_id,
                    "seat_code": f"{row}{letter}",
                    "seat_class": s_class,
                    "price": float(default_price * multiplier),
                    "seat_status": SeatStatus.free,
                }
            )
            seat_count += 1

        return seat_data
