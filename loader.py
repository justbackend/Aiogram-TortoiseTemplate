from aiogram import Bot, Dispatcher
from tortoise import Tortoise


from app.db.db import TORTOISE_ORM
from app.services import broadcaster




dp = Dispatcher()

async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Bot is started")
    await Tortoise.init(config=TORTOISE_ORM)