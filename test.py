from bs4 import BeautifulSoup
import Seecret
from IVGU.Ivgu import Ivgu
from IVGU.Table.TableConvertor import TableConvertor
tbc = TableConvertor()
ivgu = Ivgu()
ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

page = ivgu.get_schedule_page(118, 6, 1, 1, 2)
tables = tbc.get_subject_tables(page)
time_tables = tbc.get_time_table(page)


# print(tbc.have_groups(tables[0]))

lessons = tbc.get_lesson_from_table(tables[0],time_tables[0])
for i in lessons:
    time = i.subject.time
    name = i.subject.name
    type = i.subject.type
    group = i.subject.group
    print(time,name,type,group)






# teacher = self.cell.get_teacher_from_cell(str(cell))
# data_time = self.cell.get_data_date_from_cell(str(cell))