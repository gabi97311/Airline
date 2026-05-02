from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.router import router as payment_router
from src.test_router import test_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код здесь выполняется ПРИ СТАРТЕ приложения
    await payment_router.connect() 
    yield
    # Код здесь выполняется ПРИ ОСТАНОВКЕ приложения
    await payment_router.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payment_router)
app.include_router(test_router)