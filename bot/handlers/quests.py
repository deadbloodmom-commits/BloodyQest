from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from bot.database.database import SessionLocal
from bot.database.users import get_user

from bot.keyboards.player import pronouns_keyboard

from bot.keyboards.quest_menu import (
    character_navigation,
    chapters_keyboard,
    quest_01_keyboard,
    quests_keyboard,
    warning_keyboard,
)

from bot.states.player import PlayerCreation

from quests.quest_01.characters import CHARACTERS


router = Router()

# =========================================================
# КНОПКА ПОСЛЕ СОЗДАНИЯ ПЕРСОНАЖА
# =========================================================

def player_created_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🕯 Перейти к главам →",
                    callback_data="quest01:chapters",
                )
            ],
            [
                InlineKeyboardButton(
                    text="← В меню квеста",
                    callback_data="quest:01",
                )
            ],
        ]
    )


# =========================================================
# СПИСОК КВЕСТОВ
# =========================================================

@router.callback_query(F.data == "menu:quests")
async def show_quests(callback: CallbackQuery):

    text = (
        "<b>🕯 КВЕСТЫ</b>\n\n"
        "Выбери историю, в которую хочешь войти.\n\n"
        "<i>Некоторые истории пока молчат. "
        "Но однажды они обязательно заговорят.</i>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=quests_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()


# =========================================================
# ЗАКРЫТЫЙ КВЕСТ
# =========================================================

@router.callback_query(F.data == "quest:locked")
async def locked_quest(callback: CallbackQuery):

    await callback.answer(
        "Эта история пока молчит...",
        show_alert=True,
    )


# =========================================================
# КВЕСТ «ШЁПОТ»
# =========================================================

@router.callback_query(F.data == "quest:01")
async def quest_01(callback: CallbackQuery):

    text = (
        "<b>🎬«По ту сторону кадра»</b>\n\n"
        "<i>Квест I</i>\n\n"
        "История, в которой не всё является тем, "
        "чем кажется на первый взгляд.\n\n"
        "Прежде чем сделать первый шаг, "
        "тебе предстоит познакомиться с теми, "
        "кого ты встретишь внутри этой истории.\n\n"
        "<i>Не спеши.</i>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=quest_01_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()


# =========================================================
# КАК ИГРАТЬ
# =========================================================

@router.callback_query(F.data == "quest01:how_to_play")
async def quest_how_to_play(callback: CallbackQuery):

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
        reply_markup=quest_01_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()


# =========================================================
# ПЕРСОНАЖИ
# =========================================================

@router.callback_query(F.data == "quest01:characters")
async def show_first_character(callback: CallbackQuery):

    await show_character(
        callback,
        0,
    )

    await callback.answer()


async def show_character(
    callback: CallbackQuery,
    index: int,
):

    character = CHARACTERS[index]
    total = len(CHARACTERS)

    text = (
        f"<b>ПЕРСОНАЖ {index + 1} ИЗ {total}</b>\n\n"
        f"<b>{character['name']}</b>\n"
        f"<i>{character['age']} лет</i>\n\n"
        f"<b>Внешность</b>\n"
        f"{character['appearance']}\n\n"
        f"<b>Характер</b>\n"
        f"{character['personality']}\n\n"
        "<i>Пока это всё, что тебе нужно знать.</i>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=character_navigation(
            current_index=index,
            total_characters=total,
        ),
        parse_mode="HTML",
    )


# =========================================================
# ПРЕДЫДУЩИЙ ПЕРСОНАЖ
# =========================================================

@router.callback_query(F.data.startswith("character:prev:"))
async def previous_character(callback: CallbackQuery):

    index = int(
        callback.data.split(":")[-1]
    )

    new_index = max(
        index - 1,
        0,
    )

    await show_character(
        callback,
        new_index,
    )

    await callback.answer()


# =========================================================
# СЛЕДУЮЩИЙ ПЕРСОНАЖ
# =========================================================

@router.callback_query(F.data.startswith("character:next:"))
async def next_character(callback: CallbackQuery):

    index = int(
        callback.data.split(":")[-1]
    )

    new_index = min(
        index + 1,
        len(CHARACTERS) - 1,
    )

    await show_character(
        callback,
        new_index,
    )

    await callback.answer()


# =========================================================
# ПРЕДУПРЕЖДЕНИЕ
# =========================================================

@router.callback_query(F.data == "quest01:warning")
async def quest_warning(callback: CallbackQuery):

    text = (
        "<b>⚠️ ПРЕДУПРЕЖДЕНИЕ</b>\n\n"
        "Перед началом прохождения тебе необходимо "
        "ознакомиться с этим предупреждением.\n\n"
        "Квест содержит элементы хоррора, "
        "напряжённые ситуации, тревожную атмосферу "
        "и неожиданные сюжетные события.\n\n"
        "<b>Если атмосфера квеста окажется для тебя "
        "слишком неприятной, прохождение можно "
        "прекратить в любой момент.</b>\n\n"
        "<i>Продолжая, ты подтверждаешь, "
        "что ознакомился(ась) с предупреждением.</i>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=warning_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()


# =========================================================
# ПРЕДУПРЕЖДЕНИЕ ПРИНЯТО
# =========================================================

@router.callback_query(F.data == "quest01:warning_accept")
async def warning_accept(
    callback: CallbackQuery,
    state: FSMContext,
):

    await state.set_state(
        PlayerCreation.waiting_for_name
    )

    text = (
        "<b>Ты ознакомился(ась) со всеми персонажами.</b>\n\n"
        "Теперь пришло время познакомиться с тобой.\n\n"
        "<i>В этой истории у тебя будет своё место.</i>\n\n"
        "<b>🩸Как тебя будут называть?</b>\n\n"
        "Напиши имя, которым ты хочешь, "
        "чтобы тебя называли во время прохождения."
    )

    await callback.message.edit_text(
        text,
        parse_mode="HTML",
    )

    await callback.answer()


# =========================================================
# ИМЯ ИГРОКА
# =========================================================

@router.message(PlayerCreation.waiting_for_name)
async def player_name(
    message: Message,
    state: FSMContext,
):

    if not message.text:
        await message.answer(
            "Пожалуйста, напиши имя текстом."
        )
        return

    name = message.text.strip()

    if not name:
        await message.answer(
            "Имя не может быть пустым."
        )
        return

    await state.update_data(
        name=name
    )

    await state.set_state(
        PlayerCreation.waiting_for_pronouns
    )

    await message.answer(
        "<b>🩸Как к тебе обращаться?</b>\n\n"
        "Выбери свой пол, вариант, который будет использовать "
        "бот во время истории.",
        reply_markup=pronouns_keyboard(),
        parse_mode="HTML",
    )


# =========================================================
# ОБРАЩЕНИЕ
# =========================================================

@router.callback_query(
    PlayerCreation.waiting_for_pronouns,
    F.data.startswith("player:pronouns:")
)
async def player_pronouns(
    callback: CallbackQuery,
    state: FSMContext,
):

    value = callback.data.split(":")[-1]

    pronouns = {
        "female": "Женское",
        "male": "Мужское",
        "neutral": "Нейтральное",
    }

    selected = pronouns.get(value)

    if selected is None:
        await callback.answer(
            "Не удалось определить вариант.",
            show_alert=True,
        )
        return

    await state.update_data(
        pronouns=selected
    )

    await state.set_state(
        PlayerCreation.waiting_for_appearance
    )

    await callback.message.edit_text(
        "<b>🩸Теперь расскажи о своей внешности.</b>\n\n"
        "Опиши себя так, как хочешь выглядеть "
        "внутри этой истории.\n\n"
        "<i>Например: волосы, глаза, одежда "
        "или другие особенности.</i>",
        parse_mode="HTML",
    )

    await callback.answer()


# =========================================================
# ВНЕШНОСТЬ
# =========================================================

@router.message(PlayerCreation.waiting_for_appearance)
async def player_appearance(
    message: Message,
    state: FSMContext,
):

    if not message.text:
        await message.answer(
            "Опиши свою внешность текстом."
        )
        return

    appearance = message.text.strip()

    if not appearance:
        await message.answer(
            "Описание внешности не может быть пустым."
        )
        return

    await state.update_data(
        appearance=appearance
    )

    await state.set_state(
        PlayerCreation.waiting_for_personality
    )

    await message.answer(
        "<b>🩸А теперь — характер.</b>\n\n"
        "Каким человеком ты хочешь быть "
        "в этой истории?\n\n"
        "<i>Спокойным, осторожным, смелым, "
        "молчаливым, любопытным или совершенно другим.</i>",
        parse_mode="HTML",
    )


# =========================================================
# ХАРАКТЕР
# =========================================================

@router.message(PlayerCreation.waiting_for_personality)
async def player_personality(
    message: Message,
    state: FSMContext,
):

    if not message.text:
        await message.answer(
            "Опиши свой характер текстом."
        )
        return

    personality = message.text.strip()

    if not personality:
        await message.answer(
            "Описание характера не может быть пустым."
        )
        return

    data = await state.get_data()

    user = await get_user(
        message.from_user.id
    )

    if user is None:
        await state.clear()

        await message.answer(
            "Не удалось найти твой профиль. "
            "Попробуй снова через /start."
        )
        return

    user.name = data["name"]
    user.pronouns = data["pronouns"]
    user.appearance = data["appearance"]
    user.personality = personality

    async with SessionLocal() as session:
        session.add(user)
        await session.commit()

    await state.clear()

    # -----------------------------------------------------
    # ПЕРСОНАЖ СОЗДАН
    # -----------------------------------------------------

    await message.answer(
        "<b>✓ ТВОЙ ПЕРСОНАЖ СОЗДАН</b>\n\n"
        f"<b>Имя:</b> {data['name']}\n"
        f"<b>Обращение:</b> {data['pronouns']}\n\n"
        "<i>Твоя история начинается здесь.</i>\n\n"
        "Теперь выбери главу, с которой начнётся "
        "твоё путешествие.",
        reply_markup=player_created_keyboard(),
        parse_mode="HTML",
    )
# =========================================================
# ВЫБОР ГЛАВЫ
# =========================================================

@router.callback_query(F.data == "quest01:chapters")
async def show_chapters(callback: CallbackQuery):

    text = (
        "<b>🕯 ШЁПОТ</b>\n\n"
        "<b>ГЛАВЫ</b>\n\n"
        "<i>🩸 История будет открываться постепенно.</i>\n\n"
        "Первая глава уже ждёт тебя.\n"
        "<b>🩸 Остальные откроются по мере прохождения.</b>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=chapters_keyboard(),
        parse_mode="HTML",
    )

    await callback.answer()

# =========================================================
# ГЛАВА I
# =========================================================

# =========================================================
# ГЛАВА I — ПЕРЕХОД В MINI APP
# =========================================================
# =========================================================
# ГЛАВА I
# =========================================================

@router.callback_query(F.data == "chapter:01")
async def chapter_01(callback: CallbackQuery):

    user = await get_user(callback.from_user.id)

    if user is None:
        await callback.answer(
            "Профиль не найден. Используй /start.",
            show_alert=True,
        )
        return

    player_name = user.name or "Незнакомец"

    from quests.quest_01.chapters.chapter_01 import (
        get_chapter_start_text,
    )

    text = get_chapter_start_text(player_name)

    await callback.message.edit_text(
        text,
        parse_mode="HTML",
    )

    await callback.answer()
# =========================================================
# ЗАКРЫТЫЕ ГЛАВЫ
# =========================================================

@router.callback_query(F.data.startswith("chapter:locked:"))
async def locked_chapter(callback: CallbackQuery):

    await callback.answer(
        "🩸Эта глава пока закрыта.\n "
        "Сначала пройди предыдущую.",
        show_alert=True,
    )