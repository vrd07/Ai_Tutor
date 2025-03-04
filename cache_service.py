import redis 
import json
import hashlib
from typing import Optional, Any

class CacheService:
    def __init__(self, redis_url="redis://localhost:6379"):
        self.redis = redis.from_url(redis_url)
        self.ttl = 86400  # 24 hours in seconds
    
    def _generate_key(self, prefix: str, data: str) -> str:
        """Generate a cache key based on the data."""
        data_hash = hashlib.md5(data.encode()).hexdigest()
        return f"{prefix}:{data_hash}"
    
    async def get_cached_response(self, prefix: str, data: str) -> Optional[Any]:
        """Get cached response if it exists."""
        key = self._generate_key(prefix, data)
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None
    
    async def cache_response(self, prefix: str, data: str, response: Any) -> None:
        """Cache a response."""
        key = self._generate_key