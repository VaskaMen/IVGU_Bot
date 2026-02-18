import threading
import time
from datetime import datetime

import schedule

import seecret

from IVGU.APIIVGU import APIIVGU
from Notify.IVGUNotify import IVGUNotify
from SQLDB.SQLDBB import SQLDBB
from ScheduleCollector import ScheduleCollector
from TelegramBot import IvguBot
from seecret import email, password

sql = SQLDBB()
ivgu_bot = IvguBot(seecret.token, sql)
api = APIIVGU(email,password)
schedcoll = ScheduleCollector(api, sql)
infs = IVGUNotify(sql, ivgu_bot.bot)

def run_bot():
    while True:
        try:
            ivgu_bot.bot.polling(none_stop=True, interval=0)
        except Exception as ex:
            if ex.__str__() == "cursor already closed":
                sql.close_connection()
                sql.connect()
                print("Cursor error, reconnect")
            print(ex)
            with open("log/log.txt", 'a', encoding='utf-8') as file:
                file.writelines(f'{datetime.now()}: \n {ex}')



def update_schedule():
    try:
        api.login(email, password)
        time.sleep(20)
        t1 = datetime.now()
        print(f"Обновление расписания {t1}")
        schedcoll.get_schedules_for_uni_number(2)
        sql.commit()
        t2 = datetime.now()
        print(f"Обновление расписания заняло {t2 - t1}")
        infs.notify_workday_changes()
    except Exception as ex:
        print(ex)


def start_schedule():
    while True:
        schedule.run_pending()
        time.sleep(10)

schedule.every(30).minutes.do(update_schedule)

threads = []
bot_thread_run = threading.Thread(target=run_bot)
schedule_collector_thread = threading.Thread(target=start_schedule)

threads.append(bot_thread_run)
threads.append(schedule_collector_thread)

def global_thread_exception_handler(args):
    print(123123123)
    with open("log/log.txt", 'a', encoding='utf-8') as f:
        f.write(f"{'='*60}\n")
        f.write(f"НЕОБРАБОТАННОЕ ИСКЛЮЧЕНИЕ В ПОТОКЕ\n")
        f.write(f"Время: {threading.get_ident()}\n")
        f.write(f"Поток: {args.thread.name if args.thread else 'Unknown'}\n")
        f.write(f"Тип исключения: {args.exc_type.__name__}\n")
        f.write(f"Сообщение: {args.exc_value}\n")
        f.write("Трассировка стека:\n")
        f.write(f"\n{'='*60}\n\n")

threading.excepthook = global_thread_exception_handler

for t in threads:
    t.start()
for t in threads:
    t.join()