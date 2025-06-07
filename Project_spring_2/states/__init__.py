from aiogram.fsm.state import State, StatesGroup

class States(StatesGroup):
    ChoosingLanguage = State()   # выбор языка
    Broadcasting = State()       # ожидание текста рассылки
    Banning = State()            # ожидание chat_id для бана
