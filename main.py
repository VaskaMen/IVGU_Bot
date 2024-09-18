import json
import time
from telebot import types
from datetime import datetime, timedelta

import telebot
from selenium.webdriver.common.by import By

from Ivgu import Ivgu
from JsonDB import JsonDB
from Lesson import Lesson
from SubjectConvertor import SubjectConvertor
from WorkDay import WorkDay
from dataclasses import asdict

ivgu = Ivgu()
ivgu.open_student_page()
time.sleep(3)
ivgu.login("miha2204n@gmail.com", "8azr25pb")
time.sleep(2)
ivgu.open_schedule()
time.sleep(2)


el = ivgu.get_schedule_lines()
sc = SubjectConvertor()
workDays: list[WorkDay] = list()

for i in el:
    d = datetime.strptime(i.get_attribute("data-date"),'%Y-%m-%d').date()

    title = i.get_attribute("title")

    workDays.append(
        WorkDay(
            lessons=sc.get_lessons(title),
            date=d
        )
    )

jdb = JsonDB()
jdb.add_new_work_days(work_days=workDays)
# bot = telebot.TeleBot('7142763014:AAHsANyInKzPyvqYs0bodnePc-XvxuLyhtU')


def lesson_print(l: list[Lesson]):
    res = f""

    for i in l:
        res += f"{i.subject.time}  {i.subject.name} {i.subject.type} \n"
        for t in i.teacher_place:
            res += f"{t.teacher} - {t.place} \n"
        res += "\n\n"
    return res


#
# @bot.message_handler(commands = ['schedule'])
# def url(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Сегодня")
#     btn2 = types.KeyboardButton('Завтра')
#     markup.add(btn1, btn2)
#     bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)
#
#
# @bot.message_handler(commands = ['schedule_all'])
# def url(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     for i in workDays:
#         btn1 = types.KeyboardButton(f"{i.date}")
#         markup.add(btn1)
#     bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Сегодня":
#             for day in workDays:
#                 if day.date == datetime.now().date():
#                     bot.send_message(message.from_user.id, lesson_print(day.lessons))
#     if message.text == "Завтра":
#             for day in workDays:
#                 if day.date == datetime.now().date() + timedelta(days=1):
#                     bot.send_message(message.from_user.id, lesson_print(day.lessons))
#
#
# bot.polling(none_stop=True, interval=0)