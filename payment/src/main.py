from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.router import router as payment_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,   # обязательно для cookie (JWT)
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(payment_router)