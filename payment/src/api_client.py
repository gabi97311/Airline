import httpx
import asyncio
from typing import Optional, Any


class ApiClient:
    def __init__(self, base_url: str): 
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=base_url, timeout=10.0)
        
    async def _make_request(self, method: str, endpoint: str, **kwargs): 
        async with httpx.AsyncClient(base_url=self.base_url, timeout=10.0) as client:
            try:
                response = await self.client.request(method, endpoint, **kwargs)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
            return None
    
    async def get_ticket(self, ticket_id: int): 
        return await self._make_request('GET',f"/ticket/{ticket_id}")
    async def send_payment_success_event(self, ticket_id: int):
        return await self._make_request('POST',f'/ticket/{ticket_id}/confirm')
    async def send_payment_failed_event(self, ticket_id: int): 
        return await self._make_request('POST'f'/ticket/{ticket_id}/cancel')