import uuid

_news_cache = {}

def store_news(text: str) -> str:
    uid = str(uuid.uuid4())
    _news_cache[uid] = text
    return uid

def get_news(uid: str) -> str:
    return _news_cache.get(uid, "Новость не найдена./ No news found")