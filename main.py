import time

import requests
import schedule
from datetime import datetime, timedelta

from urllib3 import request

from Ivgu import Ivgu
from JsonDB import JsonDB
from SubjectConvertor import SubjectConvertor
from WorkDay import WorkDay

def update_sche():
    ivgu = Ivgu()
    ivgu.login("miha2204n@gmail.com", "8azr25pb")

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
    jdb = JsonDB()
    jdb.add_new_work_days(work_days=work_days)

update_sche()
schedule.every(30).minutes.do(update_sche)
while True:
    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as ex:
        print(ex)





# https://uni.ivanovo.ac.ru/index.php/ajaxapi?action=get_lectures_form_student&date=2024-09-20&stud_id=12618