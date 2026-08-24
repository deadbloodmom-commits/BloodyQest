import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_TOKEN
from database import init_db, get_user, save_user_profile, update_sound_setting
from quests.quest_1.data import QUEST_1_INFO, CHARACTERS_QUEST_1

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class ProfileForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_gender = State()
    waiting_for_appearance = State()
    waiting_for_personality = State()
    waiting_for_photo = State()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
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
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="† Хорошо †", callback_data="start_good")]
        ]
    )
    
    await message.answer(welcome_text, parse_mode="HTML", reply_markup=keyboard)

@dp.callback_query(F.data == "start_good")
async def process_good(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "<b>🕯 КВЕСТЫ</b>\n\n"
        "Перед тобой — несколько историй.\n"
        "У каждой свой путь, свои тайны и то, что лучше было никогда не тревожить.\n\n"
        "Выбери ту, которая первой привлекла твоё внимание.\n"
        "Но помни: истории здесь не заканчиваются там, где заканчивается текст.\n\n"
        "Иногда выбор всего одной кнопки меняет всё.\n\n"
        "Какую историю ты готов открыть?\n\n"
        "<i>Некоторые истории пока молчат. "
        "Но однажды они обязательно заговорят.</i>",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="▶️ Квест 1", callback_data="quest_1_menu")],
                [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_start")]
            ]
        )
    )
    await callback.answer()

@dp.callback_query(F.data == "quest_1_menu")
async def quest_1_menu(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    
    # Если пользователь еще не заполнял профиль
    if not user or not user["name"] or not user["gender"]:
        await callback.message.edit_text(
            "<b>Ты еще не знаком(а) с этим миром.</b>\n\n"
            "Пришло время оставить свой след.\n\n"
            "<i>В этой истории у тебя будет своё место.</i>\n\n"
            "<b>🩸 Как тебя будут называть?</b>\n\n"
            "Напиши имя, которым ты хочешь, "
            "чтобы тебя называли во время прохождения.",
            parse_mode="HTML"
        )
        await state.set_state(ProfileForm.waiting_for_name)
    else:
        # Если профиль есть — показываем полноценное меню первого квеста
        await callback.message.edit_text(
            f"<b>{QUEST_1_INFO['title']}</b>\n\n"
            f"<i>{QUEST_1_INFO['description']}</i>\n\n"
            "Выберите нужное действие:",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="📖 Как играть", callback_data="q1_how_to_play")],
                    [InlineKeyboardButton(text="👥 Ознакомиться с персонажами", callback_data="q1_char_0")],
                    [InlineKeyboardButton(text="▶️ Продолжить / Запустить", callback_data="q1_launch")],
                    [InlineKeyboardButton(text="🔙 К выбору квестов", callback_data="start_good")]
                ]
            )
        )
    await callback.answer()

# Кнопка «Как играть»
@dp.callback_query(F.data == "q1_how_to_play")
async def q1_how_to_play(callback: types.CallbackQuery):
    await callback.message.edit_text(
        QUEST_1_INFO["how_to_play"],
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🔙 Назад в меню квеста", callback_data="quest_1_menu")]
            ]
        )
    )
    await callback.answer()

# Ознакомление с персонажами по очереди (индекс 0 — первый персонаж)
@dp.callback_query(F.data.startswith("q1_char_"))
async def show_character(callback: types.CallbackQuery):
    index = int(callback.data.split("_")[2])
    
    if index < len(CHARACTERS_QUEST_1):
        char = CHARACTERS_QUEST_1[index]
        text = (
            f"🦇 <b>Персонаж {index + 1} из {len(CHARACTERS_QUEST_1)}</b>\n\n"
            f"👤 <b>Имя:</b> {char['name']}\n"
            f"🛡️ <b>Роль:</b> {char['role']}\n\n"
            f"<i>{char['bio']}</i>"
        )
        
        # Если есть еще персонажи — ведем на следующего, если кончились — на дисклеймер
        next_callback = f"q1_char_{index + 1}" if index + 1 < len(CHARACTERS_QUEST_1) else "q1_disclaimer"
        
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="▶️ Продолжить", callback_data=next_callback)],
                [InlineKeyboardButton(text="🔙 Назад", callback_data="quest_1_menu")]
            ]
        )
        
        await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()

# Дисклеймер (Предупреждение) после всех персонажей — обязательный шаг
@dp.callback_query(F.data == "q1_disclaimer")
async def show_disclaimer(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🩸 Идти дальше", callback_data="q1_launch")],
            [InlineKeyboardButton(text="🔙 К персонажам", callback_data="q1_char_0")]
        ]
    )
    
    await callback.message.edit_text(
        QUEST_1_INFO["disclaimer"],
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await callback.answer()

# Запуск / переход к мини-приложению
@dp.callback_query(F.data == "q1_launch")
async def launch_quest_webapp(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🖤 Открыть мини-приложение квеста", callback_data="open_app_stub")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="quest_1_menu")]
        ]
    )
    
    await callback.message.edit_text(
        "<b>⛓️ Врата открыты...</b>\n\n"
        "Нажмите кнопку ниже, чтобы войти в мини-приложение и начать погружение.",
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await callback.answer()

@dp.callback_query(F.data == "open_app_stub")
async def open_app_stub(callback: types.CallbackQuery):
    await callback.answer("Мини-приложение скоро будет подключено! 🕯️", show_alert=True)

@dp.message(ProfileForm.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Женский ♀", callback_data="gender_female"),
                InlineKeyboardButton(text="Мужской ♂", callback_data="gender_male"),
                InlineKeyboardButton(text="Другой ∞", callback_data="gender_other")
            ]
        ]
    )
    
    await message.answer(
        "✞ Выбери свой пол, вариант, который будет использовать "
        "бот во время истории. ✞",
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await state.set_state(ProfileForm.waiting_for_gender)

@dp.callback_query(F.data.startswith("gender_"))
async def process_gender(callback: types.CallbackQuery, state: FSMContext):
    gender_map = {
        "gender_female": "Женский",
        "gender_male": "Мужской",
        "gender_other": "Другой"
    }
    selected_gender = gender_map.get(callback.data, "Не указан")
    await state.update_data(gender=selected_gender)
    
    await callback.message.edit_text(
        "<b>🩸 Теперь расскажи о своей внешности.</b>\n\n"
        "Опиши себя так, как хочешь выглядеть "
        "внутри этой истории.\n\n"
        "<i>Например: волосы, глаза, одежда "
        "или другие особенности.</i>",
        parse_mode="HTML"
    )
    await state.set_state(ProfileForm.waiting_for_appearance)
    await callback.answer()

@dp.message(ProfileForm.waiting_for_appearance)
async def process_appearance(message: types.Message, state: FSMContext):
    await state.update_data(appearance=message.text)
    
    await message.answer(
        "<b>🩸 А теперь — характер.</b>\n\n"
        "Каким человеком ты хочешь быть "
        "в этой истории?\n\n"
        "<i>Спокойным, осторожным, смелым, "
        "молчаливым, любопытным или совершенно другим.</i>",
        parse_mode="HTML"
    )
    await state.set_state(ProfileForm.waiting_for_personality)

@dp.message(ProfileForm.waiting_for_personality)
async def process_personality(message: types.Message, state: FSMContext):
    await state.update_data(personality=message.text)
    
    await message.answer(
        "<b>★ 👁️ Отправь фотографию для своего профиля:</b>\n"
        "<i>Это лицо увидят во тьме...</i>",
        parse_mode="HTML"
    )
    await state.set_state(ProfileForm.waiting_for_photo)

@dp.message(ProfileForm.waiting_for_photo, F.photo)
async def process_photo(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    data = await state.get_data()
    
    user_id = message.from_user.id
    await save_user_profile(
        user_id,
        data.get("name"),
        data.get("gender"),
        data.get("appearance"),
        data.get("personality"),
        photo_id
    )
    await state.clear()
    
    success_text = (
        "† <b>Твой образ во тьме запечатлен.</b> †\n\n"
        f"👤 <b>Имя:</b> {data.get('name')}\n"
        f"⚧ <b>Пол:</b> {data.get('gender')}\n"
        f"🪞 <b>Внешность:</b> {data.get('appearance')}\n"
        f"🖤 <b>Характер:</b> {data.get('personality')}\n\n"
        "<i>Двери квеста открываются...</i> 🚪🩸"
    )
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="★ Перейти к Квесту №1 ★", callback_data="quest_1_menu")]
        ]
    )
    
    await message.answer_photo(photo=photo_id, caption=success_text, parse_mode="HTML", reply_markup=keyboard)

@dp.message(ProfileForm.waiting_for_photo)
async def process_photo_invalid(message: types.Message):
    await message.answer("⚠️ <b>Пожалуйста, отправь именно фотографию!</b>", parse_mode="HTML")

@dp.message(Command("settings"))
async def cmd_settings(message: types.Message):
    user = await get_user(message.from_user.id)
    sound_status = "🔊 Включены" if (not user or user["sound_enabled"] == 1) else "🔇 Выключены"
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"Звук в приложении: {sound_status}", callback_data="toggle_sound")],
            [InlineKeyboardButton(text="🔙 Закрыть", callback_data="close_settings")]
        ]
    )
    
    await message.answer("<b>⚙️ Настройки бота и мини-приложения</b>", parse_mode="HTML", reply_markup=keyboard)

@dp.callback_query(F.data == "toggle_sound")
async def toggle_sound_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    current_sound = user["sound_enabled"] if user else 1
    new_sound = 0 if current_sound == 1 else 1
    
    if not user:
        await save_user_profile(user_id, None, None, None, None, None)
    
    await update_sound_setting(user_id, new_sound)
    
    sound_status = "🔊 Включены" if new_sound == 1 else "🔇 Выключены"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"Звук в приложении: {sound_status}", callback_data="toggle_sound")],
            [InlineKeyboardButton(text="🔙 Закрыть", callback_data="close_settings")]
        ]
    )
    
    await callback.message.edit_reply_markup(reply_markup=keyboard)
    await callback.answer(f"Звук {'включен' if new_sound == 1 else 'выключен'}")

@dp.callback_query(F.data == "close_settings")
async def close_settings(callback: types.CallbackQuery):
    await callback.message.delete()

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())