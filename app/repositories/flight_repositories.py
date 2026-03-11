from sqlalchemy.orm import Session
from sqlalchemy import RowMapping, Sequence, func, select, asc, desc, update, insert
from app.schemes.flight_schemes import FlightQuery, FlightCreate
from app.models.flight_models import Flight as fl
from app.models.seat_model import FlightSeat as fs, SeatStatus

class FlightRepositories:
    def __init__(self, session: Session):
        self.session = session 
    
    def get_flight_by_id(self, flight_id:int) -> fl | None: 
       return self.session.get(fl,flight_id)
        
    def get_flight_list(self, query:FlightQuery) -> Sequence[RowMapping]: 
        
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
            stmt = stmt.where(fs.seat_class == query.ticket_class)
        
        stmt.group_by(fl.flight_id)
            
        if query.sort_by == 'price':
        
            order_func = desc('min_price') if query.sort_order == 'desc' else asc('min_price')
            stmt = stmt.order_by(order_func)
        elif query.sort_by == 'flight_date':
            stmt = stmt.order_by(fl.flight_date)
            
        offset_value = (query.page - 1) * query.size
        stmt = stmt.limit(query.size).offset(offset_value)
        
        result = self.session.execute(stmt)
    
        return result.mappings().all()
        
    def create_flight(self, flight_details: FlightCreate) -> fl:
        stmt = (insert(fl)
                .values(**flight_details.model_dump())
                .returning(fl)
                )
        result = self.session.execute(stmt)
        flight = result.scalar_one()
        return flight
        
        
        


        