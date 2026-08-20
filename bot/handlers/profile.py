from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.keyboards.profile_menu import profile_keyboard
from bot.states.player import PlayerCreation


router = Router()


@router.callback_query(F.data == "menu:profile")
async def open_profile(
    callback: CallbackQuery,
):
    await callback.message.edit_text(
        "<b>👤 ПРОФИЛЬ</b>\n\n"
        "Здесь ты можешь изменить данные своего персонажа.",
        reply_markup=profile_keyboard(),
    )

    await callback.answer()


@router.callback_query(F.data == "profile:change_name")
async def change_name(
    callback: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(
        PlayerCreation.waiting_for_name
    )

    await callback.message.edit_text(
        "<b>✏️ ИЗМЕНЕНИЕ ИМЕНИ</b>\n\n"
        "Напиши новое имя.\n\n"
        "<i>Именно так тебя будут называть "
        "в дальнейшем.</i>"
    )

    await callback.answer()


@router.callback_query(F.data == "profile:change_appearance")
async def change_appearance(
    callback: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(
        PlayerCreation.waiting_for_appearance
    )

    await callback.message.edit_text(
        "<b>✏️ ИЗМЕНЕНИЕ ВНЕШНОСТИ</b>\n\n"
        "Опиши внешность своего персонажа."
    )

    await callback.answer()


@router.callback_query(F.data == "profile:change_personality")
async def change_personality(
    callback: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(
        PlayerCreation.waiting_for_personality
    )

    await callback.message.edit_text(
        "<b>🧠 ИЗМЕНЕНИЕ ХАРАКТЕРА</b>\n\n"
        "Опиши характер своего персонажа."
    )

    await callback.answer()


@router.callback_query(F.data == "profile:change_photo")
async def change_photo(
    callback: CallbackQuery,
    state: FSMContext,
):
    await state.set_state(
        PlayerCreation.waiting_for_photo
    )

    await callback.message.edit_text(
        "<b>📷 ИЗМЕНЕНИЕ ФОТО ПРОФИЛЯ</b>\n\n"
        "Отправь новое фото персонажа."
    )

    await callback.answer()