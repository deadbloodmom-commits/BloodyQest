from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.main_menu import main_menu_keyboard
from bot.keyboards.quest_menu import quests_keyboard


router = Router()


@router.callback_query(F.data == "menu:main")
async def main_menu(callback: CallbackQuery):

    text = (
        "<b>🕯 ШЁПОТ</b>\n\n"
        "<i>🩸 Ну что, душа моя.\n"
"Выбирай свой путь.)</i>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()


@router.callback_query(F.data == "menu:quests")
async def quests_menu(callback: CallbackQuery):

    text = (
        "<b>🕯 КВЕСТЫ</b>\n\n"
        "🕯️ Выбери историю\n\n"
"Перед тобой — несколько историй.\n"
"У каждой свой путь, свои тайны и то, что лучше было никогда не тревожить.\n\n"
"Выбери ту, которая первой привлекла твоё внимание.\n"
"Но помни: истории здесь не заканчиваются там, где заканчивается текст.\n\n"
"Иногда выбор всего одной кнопки меняет всё.\n\n"
"Какую историю ты готов открыть?"
    )

    await callback.message.edit_text(
        text,
        reply_markup=quests_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()


@router.callback_query(F.data == "menu:how_to_play")
async def how_to_play(callback: CallbackQuery):

    text = (
        "<b>🕯️ КАК ИГРАТЬ</b>\n\n"
        "Твоя задача — проходить историю, искать подсказки, разгадывать загадки и принимать решения.\n\n"
"🔎Исследуй — внимательно читай сообщения и обращай внимание на детали. Иногда важная подсказка скрыта там, где её совсем не ждёшь.\n\n"
"🧩Решай — тебе будут встречаться загадки, шифры и различные задания. Не спеши с ответом.\n\n"
"🗝️Выбирай — некоторые ситуации потребуют от тебя решения. Твой выбор может повлиять на дальнейшее развитие истории.\n\n"
"📖Следи за сюжетом — запоминай найденные предметы, имена, места и подсказки. Они могут пригодиться позже.\n\n"
"⚠️Не пропускай сообщения — в квесте каждая деталь может оказаться важной.\n\n"
"Если не знаешь, что делать дальше — внимательно перечитай последние сообщения. Возможно, ответ уже находится перед тобой.\n\n"
"И главное…\n"
"<b>🕯️Не доверяй всему, что видишь.</b>\n\n"
"Удачи. Она тебе понадобится."
    )

    await callback.message.edit_text(
        text,
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()