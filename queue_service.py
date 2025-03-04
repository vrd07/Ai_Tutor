# backend/app/services/queue_service.py
import asyncio
from collections import deque
from typing import Dict, Any, Callable, Awaitable, Optional

class RequestQueue:
    def __init__(self, max_concurrent=5):
        self.max_concurrent = max_concurrent
        self.current_count = 0
        self.queue = deque()
        self.semaphore = asyncio.Semaphore(max_concurrent)
        
    async def enqueue(self, func: Callable[..., Awaitable[Any]], *args, **kwargs) -> Any:
        """Enqueue a request and execute when resources are available."""
        async with self.semaphore:
            return await func(*args, **kwargs)

