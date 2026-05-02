import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_table
from app.config import settings
from app.routers.auth_router import router as auth_router
from app.routers.user_router import router as user_router
from app.routers.ticket_router import router as ticket_router
from app.routers.seat_router import router as seat_router
from app.routers.flight_router import router as flight_router
from app.routers.airplane_router import router as airplane_router
from app.routers.broker import router as broker_router

from app.routers.analytics_router import router as analytics_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker_router.connect() 
    yield
    await broker_router.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(ticket_router)
app.include_router(seat_router)
app.include_router(flight_router)
app.include_router(airplane_router)
app.include_router(analytics_router)
app.include_router(broker_router)

