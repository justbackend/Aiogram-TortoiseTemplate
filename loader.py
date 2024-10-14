from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from tortoise import Tortoise


from tgbot.config import settings
from tgbot.db.db import TORTOISE_ORM
from tgbot.services import broadcaster



storage = RedisStorage.from_url(
    settings.redis_url
)

dp = Dispatcher(storage=storage)

async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Bot is started")
    await Tortoise.init(config=TORTOISE_ORM)