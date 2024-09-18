import telebot
from telebot import types

bot = telebot.TeleBot('7142763014:AAHsANyInKzPyvqYs0bodnePc-XvxuLyhtU')

@bot.message_handler(commands = ['schedule'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сегодня")
    btn2 = types.KeyboardButton('Завтра')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)


@bot.message_handler(commands = ['schedule_all'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in workDays:
        btn1 = types.KeyboardButton(f"{i.date}")
        markup.add(btn1)
    bot.send_message(message.from_user.id, "На какой день вы хотите увидеть расписание", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Сегодня":
            for day in workDays:
                if day.date == datetime.now().date():
                    bot.send_message(message.from_user.id, lesson_print(day.lessons))
    if message.text == "Завтра":
            for day in workDays:
                if day.date == datetime.now().date() + timedelta(days=1):
                    bot.send_message(message.from_user.id, lesson_print(day.lessons))


bot.polling(none_stop=True, interval=0)