from fastapi import HTTPException, status

class FlightErrors: 
    TICKET_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ticket not found')