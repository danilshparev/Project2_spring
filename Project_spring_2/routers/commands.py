from aiogram import Router, types
from aiogram.filters import Command
from routers.handlers import news_handler, analysis_handler, history_handler, admin_handler

router = Router()
router.include_router(news_handler.router)
router.include_router(analysis_handler.router)
router.include_router(history_handler.router)
router.include_router(admin_handler.router)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я CryptoNews Insight Bot. Напиши /news чтобы получить свежие новости. Hi! I'm CryptoNews Insight Bot. Type /news to get last news")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Доступные команды:\n/news — Получить свежие крипто-новости\n/analyze — Анализ новости\n/history — История запросов")

@router.message(Command("language"))
async def cmd_language(message: types.Message):
    await message.answer("Выберите язык:\n(функция не реализована в командах, но зато нейронка на двух языках работает:D)")