from telebot import TeleBot, types

from Notify.NotifyMessage import Notify
from Notify.NotifyTypes import NotifyTypes


class NotifySystem:
    users_notify: dict[int, Notify] = {}

    def __init__(self, bot:  TeleBot):
        self.bot = bot

    def send_users_notify(self):
        for user_id in self.users_notify:
            self.send_notify(user_id, self.users_notify[user_id])

    def send_notify(self,user_id: int, notify: Notify):
        notify_type = notify.notify_type

        if notify_type == NotifyTypes.Text:
            self.bot.send_message(user_id, notify.text)
        if notify_type == NotifyTypes.WorkdayChanges:
            self.bot.send_message(user_id, notify.text, reply_markup=notify.reply_buttons)
