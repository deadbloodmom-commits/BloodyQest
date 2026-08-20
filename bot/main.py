import asyncio

from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN

from bot.database.database import engine
from bot.database.models import Base

from bot.handlers.start import router as start_router
from bot.handlers.menu import router as menu_router
from bot.handlers.quests import router as quests_router
from bot.handlers.profile import router as profile_router
from bot.handlers.settings import router as settings_router


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def main():
    await create_tables()

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(quests_router)
    dp.include_router(profile_router)
    dp.include_router(settings_router)

    print("🕯 ШЁПОТ запущен.")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())