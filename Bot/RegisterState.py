from telebot.states import StatesGroup, State


class RegisterState(StatesGroup):
    institute = State()
    department = State()
    form = State()
    level = State()
    course = State()
    direction = State()
    subdirection = State()
    subgroup = State()
    save = State()
    done = State()