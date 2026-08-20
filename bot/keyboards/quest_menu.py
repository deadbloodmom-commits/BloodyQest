from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)

# =========================================================
# СПИСОК КВЕСТОВ
# =========================================================

def quests_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎬«По ту сторону кадра» — Квест I",
                    callback_data="quest:01",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔒 Скоро...",
                    callback_data="quest:locked",
                )
            ],
            [
                InlineKeyboardButton(
                    text="← Назад",
                    callback_data="menu:main",
                )
            ],
        ]
    )


# =========================================================
# МЕНЮ КВЕСТА «ШЁПОТ»
# =========================================================

def quest_01_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👥 Ознакомиться с персонажами",
                    callback_data="quest01:characters",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📖 Как играть",
                    callback_data="quest01:how_to_play",
                )
            ],
            [
                InlineKeyboardButton(
                    text="▶️ Продолжить",
                    callback_data="quest01:chapters",
                )
            ],
            [
                InlineKeyboardButton(
                    text="← Назад",
                    callback_data="menu:quests",
                )
            ],
        ]
    )

# =========================================================
# МЕНЮ ГЛАВ
# =========================================================

def chapters_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🕯 Глава I — Начало",
                    web_app=WebAppInfo(
                        url="https://vibrant-charm-production-87ad.up.railway.app"
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔒 Глава II",
                    callback_data="chapter:locked:02",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔒 Глава III",
                    callback_data="chapter:locked:03",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔒 Глава IV",
                    callback_data="chapter:locked:04",
                )
            ],
            [
                InlineKeyboardButton(
                    text="← Назад",
                    callback_data="quest:01",
                )
            ],
        ]
    )
# =========================================================
# ПЕРСОНАЖИ
# =========================================================

def character_navigation(
    current_index: int,
    total_characters: int,
):

    buttons = []

    if current_index > 0:
        buttons.append(
            InlineKeyboardButton(
                text="← Назад",
                callback_data=f"character:prev:{current_index}",
            )
        )

    if current_index < total_characters - 1:
        buttons.append(
            InlineKeyboardButton(
                text="Далее →",
                callback_data=f"character:next:{current_index}",
            )
        )
    else:
        buttons.append(
            InlineKeyboardButton(
                text="Продолжить →",
                callback_data="quest01:warning",
            )
        )

    return InlineKeyboardMarkup(
        inline_keyboard=[
            buttons,
            [
                InlineKeyboardButton(
                    text="✕ Выйти",
                    callback_data="quest:01",
                )
            ],
        ]
    )


# =========================================================
# ПРЕДУПРЕЖДЕНИЕ
# =========================================================

def warning_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Я ознакомился(ась) →",
                    callback_data="quest01:warning_accept",
                )
            ],
            [
                InlineKeyboardButton(
                    text="← Назад",
                    callback_data="quest01:characters",
                )
            ],
        ]
    )