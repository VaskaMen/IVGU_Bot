from ScheduleCollector import ScheduleCollector

schedcoll = ScheduleCollector()

# try:
smth = schedcoll.get_schedules_for_uni_number(2)
# schedcoll.get_schedules_for_institute(116)
# schedcoll.get_schedules_for_institute(114)
# except Exception as ex:
schedcoll.commit()