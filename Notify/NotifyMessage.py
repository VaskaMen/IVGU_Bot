from telebot.types import ReplyKeyboardMarkup

from NotifyTypes import NotifyTypes


class Notify:
    reply_buttons: ReplyKeyboardMarkup = None

    def __init__(self, notify_type: NotifyTypes, text: str):
        self.notify_type = notify_type
        self.text = text

    def set_reply_buttons(self, buttons: ReplyKeyboardMarkup):
        self.reply_buttons = buttons