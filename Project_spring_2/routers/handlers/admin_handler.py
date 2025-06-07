from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from filters.admin_filter import AdminFilter
from states.admin_states import BroadcastState, BanState
from storage.user_registry import users_db, banned_users
router = Router()


@router.message(AdminFilter(), Command("stats"))
async def cmd_stats(message: types.Message):
    try:
        with open("bot.log", "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        await message.answer(f"Логов: {len(lines)}\n Пользователей: {len(users_db)}\n Забанено: {len(banned_users)}")
    except Exception as e:
        await message.answer(f"stats error: {str(e)}")


@router.message(AdminFilter(), Command("broadcast"))
async def start_broadcast(message: types.Message, state: FSMContext):
    await message.answer("Введите текст рассылки:")
    await state.set_state(BroadcastState.waiting_for_text)


@router.message(BroadcastState.waiting_for_text)
async def process_broadcast(message: types.Message, state: FSMContext):
    await message.answer("Рассылаю...")
    text = message.text
    sent = 0
    failed = 0

    for user_id in users_db:
        if user_id in banned_users:
            continue
        try:
            await message.bot.send_message(chat_id=user_id, text=text)
            sent += 1
        except:
            failed += 1

    await message.answer(f"Рассылка завершена.\nУспешно: {sent} Ошибок: {failed}")
    await state.clear()


@router.message(AdminFilter(), Command("ban"))
async def start_ban(message: types.Message, state: FSMContext):
    await message.answer("Введите user_id для бана:")
    await state.set_state(BanState.waiting_for_user_id)


@router.message(BanState.waiting_for_user_id)
async def process_ban(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text.strip())
        banned_users.add(user_id)
        await message.answer(f"Пользователь {user_id} забанен.")
    except:
        await message.answer("Неверный ID")
    await state.clear()