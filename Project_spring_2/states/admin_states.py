from aiogram.fsm.state import State, StatesGroup

class BroadcastState(StatesGroup):
    waiting_for_text = State()

class BanState(StatesGroup):
    waiting_for_user_id = State()