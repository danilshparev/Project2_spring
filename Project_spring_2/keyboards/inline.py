from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.cache import store_news

def get_analysis_buttons(news_text: str):
    news_id = store_news(news_text)
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Анализ от DeepSeek (RU)", callback_data=f"analyze_ru:{news_id}")],
        [InlineKeyboardButton(text="Analysis from DeepSeek (EN)", callback_data=f"analyze_en:{news_id}")]
    ])
