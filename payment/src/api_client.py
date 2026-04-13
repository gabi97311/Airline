import httpx
import asyncio
from typing import Optional, Any
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
    
    async def get_ticket(self, ticket_id: int, user_id: int): 
        ticket = None 
        params = {'user_id': user_id}
        ticket = await self._make_request('POST', f"/ticket/{ticket_id}/payment-details", params=params)

        
        return ticket
        
    async def send_payment_success_event(self, ticket_id: int):
        return await self._make_request('POST',f'/ticket/{ticket_id}/confirm')
    
    async def send_payment_failed_event(self, ticket_id: int): 
        return await self._make_request('POST'f'/ticket/{ticket_id}/cancel')