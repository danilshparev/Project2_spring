from aiogram import Router
from aiogram.types import CallbackQuery
from services.api_client import analyze_news
from services.cache import get_news
from services.history import save_history

router = Router()

@router.callback_query(lambda c: c.data.startswith("analyze_ru:") or c.data.startswith("analyze_en:"))
async def handle_analysis(callback: CallbackQuery):
    lang = "ru" if callback.data.startswith("analyze_ru:") else "en"
    news_id = callback.data.split(":", 1)[1]

    news_text = get_news(news_id)
    prompt_suffix = "Ответь на русском сообщением как обычный голый текст." if lang == "ru" else "Respond in English in plain text only."
    prompt = f"Проанализируй новость: {news_text}\n\n{prompt_suffix}"

    await callback.message.answer("Отправляем в AI...")
    result = await analyze_news(prompt)

    save_history(callback.from_user.id, result)

    await callback.message.answer(result)