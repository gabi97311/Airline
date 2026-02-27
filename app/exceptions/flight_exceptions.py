from fastapi import HTTPException, status

class FlightErrors: 
    TICKET_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ticket not found')
    SEATS_NOT_AVAILABLE = HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Seats are already occupied')