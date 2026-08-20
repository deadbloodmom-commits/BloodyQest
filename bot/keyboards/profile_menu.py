from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def profile_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✏️ Изменить имя",
                    callback_data="profile:change_name",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✏️ Изменить внешность",
                    callback_data="profile:change_appearance",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✏️ Изменить характер",
                    callback_data="profile:change_personality",
                )
            ],
            [
                InlineKeyboardButton(
                    text="← Главное меню",
                    callback_data="menu:main",
                )
            ],
        ]
    )