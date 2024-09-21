import re
import threading
import time
from datetime import datetime, timedelta

import schedule
import telebot
from telebot import types

from WorkDaysDB import WorkDaysDB
from ScheduleObject.WorkDay import WorkDay


bot = telebot.TeleBot('7142763014:AAHsANyInKzPyvqYs0bodnePc-XvxuLyhtU')

workDays: list[WorkDay] = list()

def lesson_print(l: WorkDay):
    res = f"***{l.date}***\n\n"

    for i in l.lessons:
        res += f"⌚  ***{i.subject.time}*** \n📘  {i.subject.name} \n🔹  ___{i.subject.type}___ \n"
        for t in i.teacher_place:
            res += f"👨‍🏫  {t.teacher} \n🚪  ***{t.place}***\n"
        res += "\n\n"
    return res

@bot.message_handler(commands = ['schedule'])
def url(message):
    print(f"{datetime.now()} send message to ", message.from_user.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сегодня")
    btn2 = types.KeyboardButton('Завтра')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)


@bot.message_handler(commands = ['schedule_all'])
def url(message):
    print(f"{datetime.now()} send message to ", message.from_user.id)
    markup = types.ReplyKeyboardMarkup()
    for i in workDays:
        if i.date >= datetime.now().date():
            btn1 = types.KeyboardButton(f"{i.date}")
            markup.add(btn1)
    bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(f"{datetime.now()} send message to ", message.from_user.id)

    if message.text == "Сегодня":
            for day in workDays:
                if day.date == datetime.now().date():
                    bot.send_message(message.from_user.id, lesson_print(day), parse_mode='Markdown')
    if message.text == "Завтра":
            for day in workDays:
                if day.date == datetime.now().date() + timedelta(days=1):
                    bot.send_message(message.from_user.id, lesson_print(day), parse_mode='Markdown')
    if chek_date_foramt(message.text):
        serch = datetime.strptime(message.text, '%Y-%m-%d').date()
        for day in workDays:
            if serch == day.date:
                bot.send_message(message.from_user.id, lesson_print(day), parse_mode='Markdown')

def chek_date_foramt(s:str):
    if re.compile(r'\d\d\d\d-\d\d-\d\d').match(s):
        return True
    else:
        return False


def update_work_days():
    global workDays
    jdb = WorkDaysDB()
    new_days = jdb.get_work_days()
    d = jdb.get_diferens_work_days(new_days, workDays)
    for i in d:
        bot.send_message(5276492925, lesson_print(i), parse_mode='Markdown')
    workDays = new_days


def run_bot():
    update_work_days()
    bot.polling(none_stop=True, interval=0)




def sche():
    while True:
            schedule.run_pending()
            time.sleep(10)


schedule.every().minute.do(update_work_days)

threads = []
t1 = threading.Thread(target=run_bot)
t2 = threading.Thread(target=sche)
threads.append(t1)
threads.append(t2)

for t in threads:
    t.start()

for t in threads:
        t.join()

