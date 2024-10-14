from redis import asyncio as aioredis

from tgbot.config import settings

redis_client =  aioredis.from_url(settings.redis_url)
