from fastapi import APIRouter
from app.depends import AnalyticsServiceDep

router = APIRouter(prefix='/analytics', tags=['Analytics'])

@router.get('/raw-events')
async def getRawEvents(analytics_service: AnalyticsServiceDep, analytics_token: str | bytes):
    return await analytics_service.get_raw_events()