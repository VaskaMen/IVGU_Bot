import time

import schedule
from datetime import datetime, timedelta

from Ivgu import Ivgu
from JsonDB import JsonDB
from SubjectConvertor import SubjectConvertor
from WorkDay import WorkDay

def update_sche():
    ivgu = Ivgu()
    ivgu.open_student_page()
    time.sleep(3)
    ivgu.login("miha2204n@gmail.com", "8azr25pb")
    time.sleep(2)
    ivgu.open_schedule()
    time.sleep(2)


    el = ivgu.get_schedule_lines()
    sc = SubjectConvertor()
    workDays: list[WorkDay] = list()

    for i in el:
        d = datetime.strptime(i.get_attribute("data-date"),'%Y-%m-%d').date()

        title = i.get_attribute("title")

        workDays.append(
            WorkDay(
                lessons=sc.get_lessons(title),
                date=d
            )
        )
    print(workDays)
    jdb = JsonDB()
    jdb.add_new_work_days(work_days=workDays)
    ivgu.close()


schedule.every().minute.do(update_sche)
while True:
    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as ex:
        print(ex)
