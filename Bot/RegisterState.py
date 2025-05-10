from telebot.states import StatesGroup, State


class RegisterState(StatesGroup):
    institute = State()
    department = State()
    direction = State()