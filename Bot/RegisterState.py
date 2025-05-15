from telebot.states import StatesGroup, State


class RegisterState(StatesGroup):
    start_registration = State()
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
    start_pre_registration = State()
    teacher = State()
    reregister_first= State()
    reregister_second = State()