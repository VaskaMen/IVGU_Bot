from rich.console import Console
import Seecret
from IVGU.APIIVGU import APIIVGU
from IVGU.Table.TableConvertor import TableConvertor
from JsonDB.WorkDaysDB import WorkDaysDB
from SQLDB.SQLDBB import SQLDBB

sqldbb = SQLDBB()
tbc = TableConvertor()
ivgu = APIIVGU(Seecret.IVGU_LOGIN,Seecret.IVGU_PASSWORD)
console = Console()
wddb = WorkDaysDB("luboe.json")

page = ivgu._get_schedule_page(118, 6, 1, 1, 2)
tables = tbc.get_subject_tables(page)
time_tables = tbc.get_time_table(page)
directions = tbc.get_names_of_all_directions(tables[0])

# wddb.add_directions_schedule(lessons_sorted)

lessons_sorted = tbc.get_direction_schedule(tables[1],time_tables[1])
for direction in lessons_sorted:
    sqldbb.add_direction(direction.direction,118)
    for day in direction.schedule:
        for lesson in direction.schedule[day].lessons:
                sqldbb.add_lesson(lesson)



institutes = ivgu.get_institutes(2)

for institute in institutes:
    departments = ivgu.get_departments(int(institutes[institute]))
    sqldbb.add_institute(int(institutes[institute]),institute)
    for department in departments:
        sqldbb.add_department(int(departments[department]),department,int(institutes[institute]))

sqldbb.commit()
console.print(lessons_sorted[0].dict())

