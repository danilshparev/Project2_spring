import aiohttp
from config.settings import settings
from openai import OpenAI
CACHE = {}

async def fetch_latest_news():
    if "news" in CACHE:
        return CACHE["news"]

    url = f"https://cryptopanic.com/api/developer/v2/posts/?auth_token={settings.CRYPTOPANIC_API_KEY}&public=true"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                text = await resp.text()
                raise Exception(f"API error {resp.status}:\n{text[:300]}")

            data = await resp.json()

            articles = []

            for item in data.get("results", []):
                title = item.get("title", "Без заголовка")
                link = item.get("url") or item.get("source", {}).get("url") or "https://cryptopanic.com/"
                articles.append({
                    "title": title,
                    "url": link
                })

            CACHE["news"] = articles[:5]
            return articles[:5]


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY,
)

async def analyze_news(prompt_text: str, lang: str = "ru") -> str:
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-prover-v2:free",
            messages=[
                {"role": "system", "content": (
                    "Ты супер пупер криптоаналитик. Отвечай кратко, структурированно, указывай затронутые токены и рекомендации по скальпингу, интрадей и среднесрочным сделкам. Текст пришли без ### "" ** вот таких знаков, просто обычный голый текст."
                    if lang == "ru"
                    else
                    "You are a  mega sigma crypto market analyst. Answer concisely. Mention affected tokens and give actionable suggestions for scalping, intraday, and mid-term investing. Send the answer without ### "" ** just bold text."
                )},
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI error: {str(e)}"