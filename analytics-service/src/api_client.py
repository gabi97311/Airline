import httpx
from fastapi import HTTPException

class ApiClient:
    def __init__(self, base_url: str): 
        self.base_url = base_url
        
    async def _make_request(self, method: str, endpoint: str, **kwargs): 
        async with httpx.AsyncClient(base_url=self.base_url, timeout=10.0) as client:
            try:
                response = await client.request(method, endpoint, **kwargs)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                print(f"Ошибка логики другого сервиса: {e.response.status_code} - {e.response.text}")
                raise HTTPException(status_code=e.response.status_code, detail="Ticket service error")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
            return None
    
    async def get_raw_events(self, token: str | bytes):
        flight_data = await self._make_request('GET', f'/analytics/raw-events')
        return flight_data