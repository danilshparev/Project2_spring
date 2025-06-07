import json
from aiogram.filters import BaseFilter
from aiogram.types import Message

class AdminFilter(BaseFilter):
    def __init__(self, users_file: str = "storage/users.json"):
        try:
            with open(users_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.admin_ids = data.get("admins", [])
        except Exception:
            self.admin_ids = []

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids
