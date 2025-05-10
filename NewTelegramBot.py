import telebot
from telebot import State, StateMemoryStorage, custom_filters, types
from telebot.states import StatesGroup
from telebot.states.sync import StateContext
from telebot.types import ReplyParameters
from telebot.states.sync.middleware import StateMiddleware

from SQLDB.SQLDBB import SQLDBB

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

class RegisterState(StatesGroup):
    institute = State()


class NewTelegramBot:

    sql = SQLDBB()

    def __init__(self, key: str):
        state_storage = StateMemoryStorage()
        self.bot = telebot.TeleBot(key,state_storage= state_storage, use_class_middlewares=True)
        self.bot.add_custom_filter(custom_filters.StateFilter(self.bot))
        self.bot.add_custom_filter(custom_filters.IsDigitFilter())
        self.bot.add_custom_filter(custom_filters.TextMatchFilter())

        # necessary for state parameter in handlers.
        self.bot.setup_middleware(StateMiddleware(self.bot))
        self.register_massage_handler()

    def register_massage_handler(self):
        @self.bot.message_handler(commands=['start'])
        def start(message: types.Message, state: StateContext):
            state.set(RegisterState.institute)
            self.bot.send_message(message.chat.id,
            """
                   Тут ты можешь получить расписание с сайта https://uni.ivanovo.ac.ru/ для группы Прикладной информатики в цифровой экономике\n
                   Расписание проверяется каждые 30 минут. При желание ты можешь подписаться на рассылку уведомлений при изменении в расписании. 
                   Для этого вызови команду:\n/subscribe_updates\n
               """)
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            institutes = self.sql.get_list_institutes()
            buttons = [types.KeyboardButton(institute) for institute in institutes]
            keyboard.add(*buttons)
            self.bot.send_message(message.from_user.id,"""Введите институт:""", reply_markup=keyboard)

        @self.bot.message_handler(state = RegisterState.institute)
        def handle_institute(message,state: StateContext):
            state.add_data(institute = message.text)
            with state.data() as data:
                institute = data.get("institute")
                self.bot.send_message(message.from_user.id,f"Вы ввели институт: {institute}")

tele_bot = NewTelegramBot("7665754490:AAH7ugdV42S3Vxlm6sUZjnY2GwKh800xRRM")

tele_bot.bot.polling(none_stop=True, interval=0)