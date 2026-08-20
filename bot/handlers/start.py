from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.users import get_or_create_user
from bot.keyboards.main_menu import main_menu_keyboard


router = Router()


@router.message(CommandStart())
async def command_start(message: Message):

    await get_or_create_user(message.from_user)

    text = (
        "<b>🩸 КРОВАВЫЙ ШЁПОТ</b>\n\n"
        "Добро пожаловать…\n\n"
        "Здесь начинается история, в которой не всё является тем, чем кажется.\n\n"
        "🔎 Тебе предстоит искать улики, разгадывать загадки "
        "и делать выбор, который может изменить ход событий.\n\n"
        "Но будь осторожен(на).\n"
        "Некоторые тайны лучше оставить нераскрытыми.\n\n"
        "<b>🕯️ Небольшое предупреждение:</b>\n"
        "Это horror-квест. Здесь могут встречаться пугающие сцены, "
        "мрачная атмосфера и неожиданные моменты.\n\n"
        "Создатель квеста не несёт ответственности за испуг, "
        "мурашки и желание проверить, заперта ли дверь. 🔒\n\n"
        "Ты готов(а) узнать, что скрывается во тьме…?\n\n"
        "<i>И помни: иногда шёпот слышен только тем, "
        "кто действительно слушает.</i> 🩸"
    )

    await message.answer(
        text,
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML",
    )