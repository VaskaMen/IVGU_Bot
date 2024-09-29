import time
from datetime import datetime

import schedule

import Seecret
from IVGU.Ivgu import Ivgu
from IVGU.ScheduleObject.WorkDay import WorkDay
from IVGU.SubjectConvertor import SubjectConvertor
from JsonDB.WorkDaysDB import WorkDaysDB


def update_sche():
    ivgu = Ivgu()
    ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

    el = ivgu.get_schedule_lines(ivgu.get_schedule_page())
    sc = SubjectConvertor()
    work_days: list[WorkDay] = list()

    for i in el:
        d = datetime.strptime(i["data-date"], '%Y-%m-%d').date()

        title = i['title']

        work_days.append(
            WorkDay(
                lessons=sc.get_lessons(title),
                date=d
            )
        )

    print(work_days[len(work_days)-1].date)
    jdb = WorkDaysDB('workDays.json')
    jdb.add_new_work_days(work_days=work_days)

update_sche()
schedule.every(10).minutes.do(update_sche)
while True:
    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as ex:
        print(ex)
