from fastapi import FastAPI

from contextlib import asynccontextmanager 

from src.flights import router as flight_router

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await 