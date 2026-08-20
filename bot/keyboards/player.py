from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def pronouns_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🩸Женский",
                    callback_data="player:pronouns:female",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🩸Мужской",
                    callback_data="player:pronouns:male",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🩸Нейтральный",
                    callback_data="player:pronouns:neutral",
                )
            ],
        ]
    )


def player_finish_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📖 Как играть",
                    callback_data="quest01:how_to_play",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Далее →",
                    callback_data="player:continue",
                )
            ],
        ]
    )