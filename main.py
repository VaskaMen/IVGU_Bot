import json
import time
from telebot import types
from datetime import datetime, timedelta

import telebot
from selenium.webdriver.common.by import By

from Ivgu import Ivgu
from JsonDB import JsonDB
from Lesson import Lesson
from SubjectConvertor import SubjectConvertor
from WorkDay import WorkDay
from dataclasses import asdict

# ivgu = Ivgu()
# ivgu.open_student_page()
# time.sleep(3)
# ivgu.login("miha2204n@gmail.com", "8azr25pb")
# time.sleep(2)
# ivgu.open_schedule()
# time.sleep(2)
#
#
# el = ivgu.get_schedule_lines()
# sc = SubjectConvertor()
# workDays: list[WorkDay] = list()
#
# for i in el:
#     d = datetime.strptime(i.get_attribute("data-date"),'%Y-%m-%d').date()
#
#     title = i.get_attribute("title")
#
#     workDays.append(
#         WorkDay(
#             lessons=sc.get_lessons(title),
#             date=d
#         )
#     )
#
jdb = JsonDB()
# jdb.add_new_work_days(work_days=workDays)
#
#
# def lesson_print(l: list[Lesson]):
#     res = f""
#
#     for i in l:
#         res += f"{i.subject.time}  {i.subject.name} {i.subject.type} \n"
#         for t in i.teacher_place:
#             res += f"{t.teacher} - {t.place} \n"
#         res += "\n\n"
#     return res

print(jdb.get_work_days())