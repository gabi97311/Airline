from fastapi import FastAPI
from payment_router import router as payment_router

app = FastAPI()

app.include_router(payment_router)