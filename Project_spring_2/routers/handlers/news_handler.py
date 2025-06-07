from aiogram import Router, types
from aiogram.filters import Command
from services.api_client import fetch_latest_news
from keyboards.inline import get_analysis_buttons

router = Router()

@router.message(Command("news"))
async def send_news(message: types.Message):
    try:
        news = await fetch_latest_news()

        if not news:
            await message.answer("Новости не найдены./News are not found")
            return

        latest = news[0]
        text = f"<b>{latest['title']}</b>\n{latest['url']}"
        await message.answer(text, reply_markup=get_analysis_buttons(text))

    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")
