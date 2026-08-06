from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core import settings, main_broker

from app.users.user_router import router as user_router
from app.tickets import router as ticket_router
from app.seats import router as seat_router
from app.flights import router as flight_router
from app.airplanes import router as airplane_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    await main_broker.connect() 
    yield
    await main_broker.close()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(ticket_router)
app.include_router(seat_router)
app.include_router(flight_router)
app.include_router(airplane_router)


