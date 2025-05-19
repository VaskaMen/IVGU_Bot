from datetime import timedelta, datetime

import seecret
from Bot.DateFunctions import DateFunctions
from Notify.IVGUNotify import IVGUNotify

from SQLDB.SQLDBB import SQLDBB
from TelegramBot import IvguBot

datefun = DateFunctions()
sql = SQLDBB()
ivgu_bot = IvguBot(seecret.token, sql)

infs = IVGUNotify(sql, ivgu_bot.bot)
infs.notify_workday_changes()


# nfs = NotifySystem(ivgu_bot.bot)
# nfs.users_notify[5276492925] = Notify(NotifyTypes.Text, "123")
# nfs.send_users_notify()