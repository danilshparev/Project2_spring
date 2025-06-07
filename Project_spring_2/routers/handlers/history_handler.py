import json
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("history"))
async def show_history(message: types.Message):
    try:
        with open("storage/history.json", "r", encoding="utf-8") as f:
            history = json.load(f).get(str(message.from_user.id), [])
        if not history:
            await message.answer("История пуста")
        else:
            for item in history[-5:]:
                await message.answer(item)
    except Exception:
        await message.answer("Не удалось загрузить историю.")