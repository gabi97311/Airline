from src.repositories import FlightCollectorRepo
class FlightCollector:
    def __init__(self, flight_repo: FlightCollectorRepo):
        self.repo = flight_repo