import re
from datetime import datetime, timedelta, date

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply

from User import User
from JsonDB.UserDB import UserDB
from JsonDB.WorkDaysDB import WorkDaysDB
from IVGU.ScheduleObject.WorkDay import WorkDay

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

class IvguBot:
    work_days_DB = WorkDaysDB("workDays.json")
    users_DB = UserDB("users.json")
    changes: list[WorkDay] = list()

    work_days: list[WorkDay] = list()
    users: list[User] = list()

    def __init__(self, key: str):
        self.bot = telebot.TeleBot(key)
        self.__load_work_days()
        self.register_massage_handler()

    def __load_work_days(self):
        self.work_days = self.work_days_DB.get_work_days()

    def convert_str_to_date(self, s: str) -> date:
        return datetime.strptime(s.split(' ')[0], '%Y-%m-%d').date()

    def update_work_days(self):
        new_days = self.work_days_DB.get_work_days()
        self.changes = self.work_days_DB.get_diferens_work_days(new_days, self.work_days)
        self.changes = self.get_only_actual_days(self.changes)
        self.work_days = new_days
        self.send_notification()

    def send_notification(self):
        self.users = self.users_DB.get_all_users()
        if len(self.changes) != 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in self.changes:
                btn = types.KeyboardButton(str(i.date))
                markup.add(btn)
            self.send_message_for_all_get_changes_users("Появилось новое расписание", markup=markup)

    def send_message_for_all_get_changes_users(self, text:str, markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None):
        for user in self.users:
            if user.get_changes:
                self.bot.send_message(user.id, text, parse_mode='Markdown', reply_markup=markup)

    def get_only_actual_days(self, days: list[WorkDay]) -> list[WorkDay]:
        actual_days: list[WorkDay] = list()
        for i in days:
            if i.date >= datetime.now().date():
                actual_days.append(i)
        return actual_days

    def get_last_days(self, count:int, days: list[WorkDay]) -> list[WorkDay]:
        return days[-count:]

    def check_date_format(self, s: str):
        if re.compile(r'\d\d\d\d-\d\d-\d\d').match(s):
            return True
        else:
            return False

    def get_work_day_date(self, d: date) -> WorkDay | None:
        for day in self.work_days:
            if day.date == d:
                return day
        return None

    def send_work_day(self, user_id, work_day: WorkDay):
        self.bot.send_message(user_id, str(work_day),parse_mode='Markdown')

    def handler_today_tomorrow(self, message):
        print(f"{datetime.now()} Send message to {message.from_user.id}")
        if message.text == "Сегодня":
            self.send_work_day(message.from_user.id, self.get_work_day_date(datetime.now().date()))
        if message.text == "Завтра":
            d = datetime.now().date() + timedelta(days=1)
            self.send_work_day(message.from_user.id, self.get_work_day_date(d))

    def handler_work_day_date(self, message):
        print(f"{datetime.now()} Send message to {message.from_user.id}")
        if self.check_date_format(message.text):
            search =  self.convert_str_to_date(message.text)
            self.send_work_day(message.from_user.id, self.get_work_day_date(search))

    def register_massage_handler(self):
        @self.bot.message_handler(commands = ['schedule'])
        def actual(message):
            print(f"{datetime.now()} Send message to {message.from_user.id}")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Сегодня")
            btn2 = types.KeyboardButton('Завтра')
            markup.add(btn1, btn2)
            self.bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)
            self.bot.register_next_step_handler(message, self.handler_today_tomorrow)


        @self.bot.message_handler(commands = ['schedule_all'])
        def schedule_all_actual(message):
            print(f"{datetime.now()} Send message to {message.from_user.id}")
            markup = types.ReplyKeyboardMarkup()
            actual = self.get_only_actual_days(self.work_days)

            for day in actual:
                btn = types.KeyboardButton(f"{day.date}")
                markup.add(btn)

            self.bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)
            self.bot.register_next_step_handler(message, self.handler_work_day_date)

        @self.bot.message_handler(commands=['schedule_history'])
        def schedule_history(message):
            print(f"{datetime.now()} Send message to {message.from_user.id}")
            markup = types.ReplyKeyboardMarkup()
            last = self.get_last_days(7, self.work_days)

            for day in last:
                btn = types.KeyboardButton(f"{day.date} {week[day.date.weekday()]}")
                markup.add(btn)

            self.bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание",
                                  reply_markup=markup)
            self.bot.register_next_step_handler(message, self.handler_work_day_date)

        @self.bot.message_handler(commands= ['subscribe_updates'])
        def subscribe_updates(message):
            self.bot.send_message(message.from_user.id, "Теперь вы будете получать уведомления при изменении в расписании. \nЧтобы отписаться от рассылки вызовете команду \n/unsubscribe_updates")
            self.users_DB.add_new_user(
                User(
                    message.from_user.id,
                    True
                )
            )

        @self.bot.message_handler(commands=['unsubscribe_updates'])
        def unsubscribe_updates(message):
            self.bot.send_message(message.from_user.id, "Вы отписались от уведомлений при изменении расписания. \nЧтобы подписаться на рассылку вызовете команду \n/subscribe_updates ")

            self.users_DB.add_new_user(
                User(
                    message.from_user.id,
                    False
                )
            )

        @self.bot.message_handler(content_types=['text'])
        def text(message):
            print(f"{datetime.now()} Send message to {message.from_user.id}")
            if self.check_date_format(message.text):
                d = self.convert_str_to_date(message.text)
                work_day = self.get_work_day_date(d)
                self.send_work_day(message.from_user.id, work_day)