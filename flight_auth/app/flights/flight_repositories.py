from app.seats import Seat as fs
from app.flights.flight_schemes import FlightQuery
from app.flights.flight_models import Flight as fl
from app.seats import SeatStatus

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import RowMapping, Sequence, func, select, asc, desc, update, insert



class FlightRepositories:
    def __init__(self, session: AsyncSession):
        self.session = session 
    
    async def get_flight_by_id(self, flight_id:int) -> fl | None: 
       return await self.session.get(fl,flight_id)
        
    async def get_flight_list(self, query:FlightQuery) -> Sequence[RowMapping]: 
        
        stmt = (select(fl,func.min(fs.price).label('min_price')).join(fl.seats).where(fs.seat_status == SeatStatus.free))
        
        #Filters of the flight 
        if query.flight_date: 
            stmt = stmt.where(fl.flight_date == query.flight_date)
        if query.origin: 
            stmt = stmt.where(fl.origin == query.origin)
        if query.dest: 
            stmt = stmt.where(fl.dest == query.dest)
            
        # filter seats 
        if query.min_price: 
            stmt = stmt.where(fs.price >= query.min_price)
        if query.max_price: 
            stmt = stmt.where(fs.price <= query.max_price)
        if query.ticket_class:
            stmt = stmt.where(fs.seat_class == query.ticket_class.capitalize())
        
        stmt.group_by(fl.flight_id)
            
        if query.sort_by == 'price':
        
            order_func = desc('min_price') if query.sort_order == 'desc' else asc('min_price')
            stmt = stmt.group_by(
                fl.flight_id, 
                fl.flight_date, 
                fl.reporting_airline, 
                fl.origin, 
                fl.dest, 
                fl.airplane_id, 
                fl.is_delay
            )
        elif query.sort_by == 'flight_date':
            stmt = stmt.order_by(fl.flight_date)
            
        offset_value = (query.page - 1) * query.size
        stmt = stmt.limit(query.size).offset(offset_value)
        
        result = await self.session.execute(stmt)
    
        return result.mappings().all()
        
    async def create_flight(self, flight:fl ) -> fl:
       self.session.add(flight)
       await self.session.flush()
       return flight 
        