from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB

sql = SQLDBB()
api = APIIVGU("miha2204n@gmail.com","8azr25pb")

all_departments = api.get_departments(113)
for department in all_departments:
    all_links = api.get_schedule_links_for_department(int(all_departments[department]))
    for link in all_links:
        course = api.get_course_from_link(link)
        level = api.get_level_from_link(link)
        page = api.get_page(link)
        schedules = api.get_schedules_from_page(page)
        for schedule in schedules:
            sql.add_direction_schedule(schedule,int(all_departments[department]),course, level)

sql.commit()

# sh = api.get_schedule(118,6,1,1,2)
# for s in sh:
#     sql.add_direction_schedule(s, 118)
"https://uni.ivanovo.ac.ru/info/showschedule/127/6/1/1/2"