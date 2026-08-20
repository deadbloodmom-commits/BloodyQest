from aiogram.fsm.state import State, StatesGroup


class PlayerCreation(StatesGroup):

    waiting_for_name = State()

    waiting_for_pronouns = State()

    waiting_for_appearance = State()

    waiting_for_personality = State()

    waiting_for_photo = State()