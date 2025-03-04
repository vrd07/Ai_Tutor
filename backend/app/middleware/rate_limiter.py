from fastapi import Request, HTTPException
import time
from typing import Dict, List

class RateLimiter:
    def __init__(self, requests_per_minute=30):
        self.requests_per_minute = requests_per_minute
        self.request_history: Dict[str, List[float]] = {}
        
    async def __call__(self, request: Request):
        client_ip = request.client.host
        current_time = time.time()
        
        # Initialize if this is a new client
        if client_ip not in self.request_history:
            self.request_history[client_ip] = []
            
        # Clean up old requests (older than 1 minute)
        self.request_history[client_ip] = [
            req_time for req_time in self.request_history[client_ip]
            if current_time - req_time < 60
        ]
        
        # Check if rate limit exceeded
        if len(self.request_history[client_ip]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please try again later."
            )
            
        # Add current request to history
        self.request_history[client_ip].append(current_time)