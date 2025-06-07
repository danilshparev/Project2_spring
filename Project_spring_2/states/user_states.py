from aiogram.fsm.state import StatesGroup, State

class AnalyzeState(StatesGroup):
    waiting_for_custom_url = State()