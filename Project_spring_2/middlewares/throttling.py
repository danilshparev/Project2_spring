from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message
import time

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit=0.5):
        super().__init__()
        self.rate_limit = rate_limit
        self.users = {}

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current = time.time()
        if user_id in self.users and current - self.users[user_id] < self.rate_limit:
            await event.answer("Подождите пару секунд и отправьте запрос еще раз")
            return
        self.users[user_id] = current
        return await handler(event, data)
