import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

if not BOT_TOKEN:
    raise ValueError("⚠️ Ошибка: BOT_TOKEN не найден в переменных окружения!")
if not DATABASE_URL:
    raise ValueError("⚠️ Ошибка: DATABASE_URL не найден в переменных окружения!")