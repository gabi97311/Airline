from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from contextlib import asynccontextmanager
from src.router import router as payment_router
from faststream.rabbit import RabbitBroker

broker = RabbitBroker(host=settings.RMQ_URL)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.start()
    yield
    await broker.close(
    )

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(payment_router)