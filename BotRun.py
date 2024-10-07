import threading
import time

import schedule

import Seecret
from TelegramBot import IvguBot

ivgu_bot = IvguBot(Seecret.BOT_TOKEN)

def run_bot():
    while True:
        try:
            ivgu_bot.update_work_days()
            ivgu_bot.bot.polling(none_stop=True, interval=0)
        except Exception as ex:
            print(ex)




def sche():
    while True:
            schedule.run_pending()
            time.sleep(10)


schedule.every().minute.do(ivgu_bot.update_work_days)

threads = []
t1 = threading.Thread(target=run_bot)
t2 = threading.Thread(target=sche)
threads.append(t1)
threads.append(t2)

for t in threads:
    t.start()

for t in threads:
        t.join()