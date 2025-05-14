import seecret
from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB
from ScheduleCollector import ScheduleCollector
from TelegramBot import IvguBot
from seecret import email, password

api = APIIVGU(email,password)
sql = SQLDBB()

# schedcoll = ScheduleCollector(api)
#
# smth = schedcoll.get_schedules_for_uni_number(2)
# schedcoll.commit()

bot = IvguBot(seecret.token, sql)
bot.bot_run()
