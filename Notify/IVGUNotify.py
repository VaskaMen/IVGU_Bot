from datetime import timedelta, datetime

from telebot import TeleBot

from Bot.BotCreator import BotCreator
from Bot.DateFunctions import DateFunctions
from Notify.NotifyMessage import Notify
from Notify.NotifySystem import NotifySystem
from Notify.NotifyTypes import NotifyTypes
from SQLDB.SQLDBB import SQLDBB


class IVGUNotify(NotifySystem):

    groups_notify: dict[int, Notify]
    datefun = DateFunctions()

    def __init__(self,sql: SQLDBB, bot: TeleBot):
        super().__init__(bot)
        self.sql = sql

    def notify_workday_changes(self):
        changes = self.workday_changes_for_group()
        self.create_group_notify_workday(changes)
        self.send_users_notify()

    def workday_changes_for_group(self) -> dict[int, list[datetime]]:
        above_date = self.sql.get_last_insert_date_workday()
        # for test
        above_date = above_date - timedelta(seconds=220)

        new_workdays = self.sql.get_workday_above_insert_date(above_date)
        group_dates: dict[int, list[datetime]] = {}

        for work_day in new_workdays:
            group_id = work_day[-1]
            if group_id not in group_dates:
                group_dates[group_id] = []
            group_dates[group_id].append(work_day[2].date())
        return  group_dates


    def create_group_notify_workday(self, group_workday: dict[int, list[datetime]]):
        for group_id in group_workday:
            reworked_dates = self.datefun.get_actual_dates(group_workday[group_id])
            buttons = BotCreator.create_text_buttons(reworked_dates, 1)
            notify = Notify(NotifyTypes.WorkdayChanges, "Новое расписание")
            notify.set_reply_buttons(buttons)
            self.set_users_notify_from_group_id(group_id, notify)

    def set_users_notify_from_group_id(self, group_id:int, notify: Notify):
        users = self.sql.get_users_with_group_id(group_id)
        for user in users:
            user_id = user[0]
            self.users_notify[user_id] = notify
