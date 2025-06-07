import json

LANG_FILE = "locales/lang.json"
DEFAULT_LANG = "ru"

with open(LANG_FILE, encoding="utf-8") as f:
    LANGS = json.load(f)

def t(key: str, lang: str = DEFAULT_LANG):
    return LANGS.get(lang, {}).get(key, key)
