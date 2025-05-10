import telebot
from telebot import StateMemoryStorage, custom_filters, types
from telebot.states.sync import StateContext, StateMiddleware

from Bot.BotCreator import BotCreator
from Bot.BotText import BotText
from Bot.RegisterState import RegisterState
from SQLDB.SQLDBB import SQLDBB

key = "7665754490:AAH7ugdV42S3Vxlm6sUZjnY2GwKh800xRRM"

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
sql = SQLDBB()

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(key,state_storage= state_storage, use_class_middlewares=True)
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.setup_middleware(StateMiddleware(bot))

@bot.message_handler(commands=['start'])
def start(message: types.Message, state: StateContext):
    state.set(RegisterState.institute)
    institutes = sql.get_list_institutes()
    bot.send_message(
        message.chat.id,
        text=BotText.start_text
    )
    bot.send_message(
        message.from_user.id,
        text=BotText.insert_institute,
        reply_markup=BotCreator.create_text_buttons(institutes)
    )

@bot.message_handler(state = RegisterState.institute)
def handle_institute(message, state: StateContext):
    state.add_data(institute = message.text)
    state.set(RegisterState.department)

    with state.data() as data:
        institute = data.get("institute")
    departments = sql.get_list_departments(institute)

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_department,
        reply_markup=BotCreator.create_text_buttons(departments)
    )

@bot.message_handler(state = RegisterState.department)
def handle_department(message, state: StateContext):
    state.add_data(department = message.text)
    state.set(RegisterState.direction)

    with state.data() as data:
        department = data.get("department")

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_direction
    )


bot.polling(none_stop=True, interval=0)