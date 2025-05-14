from IVGU.APIIVGU import APIIVGU
from ScheduleCollector import ScheduleCollector
from seecret import email, password

api = APIIVGU(email,password)

schedcoll = ScheduleCollector(api)

smth = schedcoll.get_schedules_for_uni_number(2)
schedcoll.commit()