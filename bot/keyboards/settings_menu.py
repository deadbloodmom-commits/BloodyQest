from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def settings_keyboard(
    sound_enabled: bool,
    music_enabled: bool,
    notifications_enabled: bool,
):

    sound = "🔊 Звуки: Вкл." if sound_enabled else "🔇 Звуки: Выкл."
    music = "🎵 Музыка: Вкл." if music_enabled else "🎵 Музыка: Выкл."
    notifications = (
        "🔔 Уведомления: Вкл."
        if notifications_enabled
        else "🔕 Уведомления: Выкл."
    )

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=sound,
                    callback_data="settings:sound",
                )
            ],
            [
                InlineKeyboardButton(
                    text=music,
                    callback_data="settings:music",
                )
            ],
            [
                InlineKeyboardButton(
                    text=notifications,
                    callback_data="settings:notifications",
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