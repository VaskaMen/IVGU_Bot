from rich.console import Console
import Seecret
from IVGU.APIIVGU import APIIVGU
from IVGU.Table.TableConvertor import TableConvertor
from SQLDB.SQLDBB import SQLDBB

sqldbb = SQLDBB()
tbc = TableConvertor()
ivgu = APIIVGU(Seecret.IVGU_LOGIN,Seecret.IVGU_PASSWORD)
console = Console()

all_links = ivgu.get_schedule_links_for_department(129)
for link in all_links:
    all_schedules = ivgu.get_schedules_from_link(link)
    for direction in all_schedules:
        sqldbb.add_direction_schedule(direction,129)

institutes = ivgu.get_institutes(2)

for institute in institutes:
    departments = ivgu.get_departments(int(institutes[institute]))
    sqldbb.add_institute(int(institutes[institute]),institute)
    for department in departments:
        sqldbb.add_department(int(departments[department]),department,int(institutes[institute]))

sqldbb.commit()

# call = ivgu.get_schedules(129,6,1,1,2)
# print(call)

