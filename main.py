import asyncio

from fastapi import FastAPI
from app.database import create_table
from app.routers.auth_router import router as auth_router
from app.routers.user_router import router as user_router
from app.routers.ticket_router import router as ticket_router
from app.routers.seat_router import router as seat_router
from app.routers.flight_router import router as flight_router
from app.routers.airplane_router import router as airplane_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(ticket_router)
app.include_router(seat_router)
app.include_router(flight_router)
app.include_router(airplane_router)

# asyncio.run(create_table())
