import threading
import time
from datetime import datetime

import schedule

import seecret
from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB
from ScheduleCollector import ScheduleCollector
from TelegramBot import IvguBot
from seecret import email, password

sql = SQLDBB()
ivgu_bot = IvguBot(seecret.token, sql)
api = APIIVGU(email,password)
schedcoll = ScheduleCollector(api, sql)

def run_bot():
    while True:
        try:
            ivgu_bot.bot.polling(none_stop=True, interval=0)
        except Exception as ex:
            print(ex)


def update_schedule():
    try:
        api.login(email, password)
        time.sleep(20)
        t1 = datetime.now()
        print(f"Обновление расписание {t1}")
        schedcoll.get_schedules_for_uni_number(2)
        sql.commit()
        t2 = datetime.now()
        print(f"Обновление расписание заняло {t2 - t1}")
    except Exception as ex:
        print(ex)


def start_schedule():
    while True:
        schedule.run_pending()
        time.sleep(10)

schedule.every(3).minutes.do(update_schedule)

threads = []
bot_thread_run = threading.Thread(target=run_bot)
schedule_collector_thread = threading.Thread(target=start_schedule)

threads.append(bot_thread_run)
threads.append(schedule_collector_thread)

for t in threads:
    t.start()
for t in threads:
    t.join()