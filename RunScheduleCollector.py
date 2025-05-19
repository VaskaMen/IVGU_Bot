from datetime import datetime

import schedule

from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB
from ScheduleCollector import ScheduleCollector
from seecret import email, password

sql = SQLDBB()
api = APIIVGU(email,password)
schedcoll = ScheduleCollector(api, sql)


def update_schedule():
    try:
        api.login(email, password)
        t1 = datetime.now()
        print(f"Обновление расписания {t1}")
        schedcoll.get_schedules_for_uni_number(2)
        sql.commit()
        t2 = datetime.now()
        print(f"Обновление расписания заняло {t2 - t1}")
    except Exception as ex:
        print(ex)

update_schedule()
schedule.every(3).minutes.do(update_schedule)

while True:
    update_schedule()
