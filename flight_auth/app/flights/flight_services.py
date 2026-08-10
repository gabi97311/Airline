import uuid
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from faststream.rabbit import RabbitBroker
from datetime import datetime

from app.seats import SeatServices
from app.airplanes import AirplaneServices

from app.flights.flight_models import Flight
from app.flights.flight_repositories import FlightRepositories
from app.flights.flight_schemes import (
    FlightQuery,
    FlightCreate,
    FlightUpdate,
)
from app.utils.enums import FlightEvent, RabbitExchange
from app.outboxes import FlightAnalyticsMessage, OutBoxService

class FlightServices:
    def __init__(
        self,
        session: AsyncSession,
        repository: FlightRepositories,
        seat_service: SeatServices,
        airplane_service: AirplaneServices,
        outbox_service: OutBoxService,
        broker: RabbitBroker,
    ):

        self.session = session
        self.repository = repository
        self.seat_service = seat_service
        self.airplane_service = airplane_service
        self.outbox_service = outbox_service
        self.broker = broker

    async def get_flight_list(self, flight_query: FlightQuery) -> list[Flight]:
        return await self.repository.get_flight_list(flight_query)

    async def get_flight_by_id(self, flight_id: int) -> Flight:
        flight = await self.repository.get_flight_by_id(flight_id)

        if not flight:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Flight not found"
            )

        return flight

    async def create_flight(self, flight_details: FlightCreate):

        if not (
            airplane := await self.airplane_service.get_airplane_by_id(
                flight_details.airplane_id
            )
        ):
            raise HTTPException(status_code=404, detail="Airplane not found")


        try:
            flight = await self.repository.create_flight(flight)
            await self.seat_service.generate_seats_for_flight(
                flight.flight_id, airplane
            )
            await self.build_flight_event(flight)
            await self.session.commit()
            await self.session.refresh(flight)
            return flight
        except Exception as e:
            await self.session.rollback()
            raise e

    async def update_flight_by_id(self, flight: FlightUpdate):
        pass

    async def build_flight_event(self, flight: Flight, event_type: FlightEvent) -> FlightAnalyticsMessage:
        message = FlightAnalyticsMessage(
            event_id=str(uuid.uuid4()),
            routing_key=event_type.value,
            event_time=datetime.utcnow(),
            version=int(datetime.utcnow().timestamp()),
            flight_id=flight.flight_id,
            flight_date=flight.flight_date,
            reporting_airline=flight.reporting_airline,
            origin=flight.origin,
            dest=flight.dest,
            is_delay=flight.is_delay,
            cancelled=flight.status,
        )
        # saves sent messages in db \ We need to set up a background process for sending a message.
        await self.outbox_service.save(message)
        return message
        
    async def _publish_flight_analytics(self, message: FlightAnalyticsMessage) -> None:
       await self.broker.publish(message, exchange=RabbitExchange.FLIGHT_EVENTS.value)