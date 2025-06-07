import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config.settings import settings
from routers import commands
from middlewares.throttling import ThrottlingMiddleware
from middlewares.user_tracker import UserTrackerMiddleware
from utils.logger import setup_logger

async def main():
    setup_logger()

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())

    # Middleware
    dp.message.middleware(ThrottlingMiddleware(rate_limit=0.5))
    dp.message.middleware(UserTrackerMiddleware())

    # Роутеры
    dp.include_router(commands.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())