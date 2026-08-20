from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.database.database import SessionLocal
from bot.database.models import User
from bot.keyboards.settings_menu import settings_keyboard

from sqlalchemy import select


router = Router()


async def get_settings_user(telegram_id: int):

    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == telegram_id
            )
        )

        return result.scalar_one_or_none()


@router.callback_query(F.data == "menu:settings")
async def settings(callback: CallbackQuery):

    user = await get_settings_user(
        callback.from_user.id
    )

    if not user:
        await callback.answer(
            "Профиль не найден.",
            show_alert=True,
        )
        return

    text = (
        "<b>⚙️ НАСТРОЙКИ</b>\n\n"
        "Здесь ты сможешь управлять звуками, "
        "музыкой и уведомлениями."
    )

    await callback.message.edit_text(
        text,
        reply_markup=settings_keyboard(
            user.sound_enabled,
            user.music_enabled,
            user.notifications_enabled,
        ),
        parse_mode="HTML",
    )

    await callback.answer()


@router.callback_query(F.data == "settings:sound")
async def toggle_sound(callback: CallbackQuery):

    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == callback.from_user.id
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            await callback.answer()
            return

        user.sound_enabled = not user.sound_enabled

        await session.commit()

        await callback.message.edit_reply_markup(
            reply_markup=settings_keyboard(
                user.sound_enabled,
                user.music_enabled,
                user.notifications_enabled,
            )
        )

    await callback.answer()


@router.callback_query(F.data == "settings:music")
async def toggle_music(callback: CallbackQuery):

    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == callback.from_user.id
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            await callback.answer()
            return

        user.music_enabled = not user.music_enabled

        await session.commit()

        await callback.message.edit_reply_markup(
            reply_markup=settings_keyboard(
                user.sound_enabled,
                user.music_enabled,
                user.notifications_enabled,
            )
        )

    await callback.answer()


@router.callback_query(F.data == "settings:notifications")
async def toggle_notifications(callback: CallbackQuery):

    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == callback.from_user.id
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            await callback.answer()
            return

        user.notifications_enabled = (
            not user.notifications_enabled
        )

        await session.commit()

        await callback.message.edit_reply_markup(
            reply_markup=settings_keyboard(
                user.sound_enabled,
                user.music_enabled,
                user.notifications_enabled,
            )
        )

    await callback.answer()