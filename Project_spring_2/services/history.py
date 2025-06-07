import json
from pathlib import Path

HISTORY_PATH = Path("storage/history.json")

def save_history(user_id: int, text: str):
    try:
        if HISTORY_PATH.exists():
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                history = json.load(f)
        else:
            history = {}

        uid = str(user_id)
        history.setdefault(uid, []).append(text)

        with open(HISTORY_PATH, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[History] Error: {e}")