from typing import Annotated
from functools import cached_property

from fastapi import Depends
from app.core import AsyncSessionDep, main_broker
from app.flights import FlightServices, FlightRepositories
from app.seats import SeatServices, SeatRepositories
from app.airplanes import AirplaneServices, AirplaneRepositories
from app.tickets import TicketServices, TicketRepositories
from app.outboxes import OutBoxService, OutBoxRepo


class ServicesContainer:
    def __init__(self, session: AsyncSessionDep):
        self.session = session

    @cached_property
    def seat(self) -> SeatServices:
        return SeatServices(self.session, SeatRepositories(self.session))

    @cached_property
    def airplane(self) -> AirplaneServices:
        return AirplaneServices(AirplaneRepositories(self.session))

    @cached_property
    def flight(self) -> FlightServices:
        return FlightServices(
            self.session,
            FlightRepositories(self.session),
            self.seat,
            self.airplane,
            self.outbox,
            main_broker,
        )

    @cached_property
    def outbox(self) -> OutBoxService:
        return OutBoxService(OutBoxRepo(self.session))

    @cached_property
    def ticket(self) -> TicketServices:
        return TicketServices(
            self.session, TicketRepositories(self.session), self.flight, self.seat
        )


Services = Annotated[ServicesContainer, Depends(ServicesContainer)]
