from fastapi import FastAPI

from src.router import router as payment_router

app = FastAPI()

app.include_router(payment_router)