import asyncio
import logging

from aiogram.client.default import DefaultBotProperties
import betterlogging as bl
from aiogram import Bot
from aiogram.methods import DeleteWebhook

from loader import dp, on_startup
from app.config import settings

from tortoise import Tortoise

async def on_shutdown():
    await Tortoise.close_connections()

def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Returns:
        None

    Example usage:
        setup_logging()
    """
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main():
    setup_logging()


    # dp.include_routers(*routers_list)

    if settings.DEBUG:
        token = settings.DEBUG_TOKEN
    else:
        token = settings.BOT_TOKEN

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode='HTML'))
    await on_startup(bot, settings.ADMINS)

    await bot(DeleteWebhook(drop_pending_updates=True))
    try:
        await dp.start_polling(bot)
    finally:
        await on_shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot has a problem!")
