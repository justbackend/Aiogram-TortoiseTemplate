import asyncio

from aiogram.exceptions import TelegramRetryAfter


async def bot_send_message(bot, **kwargs):
    try:
        response = await bot.send_message(**kwargs)
    except TelegramRetryAfter as e:
        await asyncio.sleep(e.retry_after)
        response = await bot.send_message(**kwargs)

    return response