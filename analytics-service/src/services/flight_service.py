from src.api_client import ApiClient
from src.repositories.flight_repo import FlightRepository
from src.jwt import encode_jwt
class FlightService:
    def __init__(self, flight_repo: FlightRepository):
        self.repo = flight_repo
    
    async def ingest_data_from_flight(self, flight_client: ApiClient):
        
        jwt_payload = {'service_name': 'analytics_service'}
        token = encode_jwt(jwt_payload)
        
        flight_data = await flight_client.get_raw_events(token)
        
        
        