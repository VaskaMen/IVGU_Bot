from bs4 import BeautifulSoup
import Seecret
from IVGU.Ivgu import Ivgu
from IVGU.Table.TableConvertor import TableConvertor
tbc = TableConvertor()
ivgu = Ivgu()
ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

page = ivgu.get_schedule_page(128, 6, 2, 2, 2)
tables = tbc.get_subject_tables(page)
time_tables = tbc.get_time_table(page)




lessons = tbc.get_lesson_from_table(tables[0],time_tables[0])
# for i in lessons:
#     time = i.subject.time
#     name = i.subject.name
#     type = i.subject.type
#     group = i.subject.group
#     print(time,name,type,group)

subgroups = {}
all_directions = tbc.get_names_of_all_directions(tables[0])


quantity = tbc.get_quantity_of_subgroups(tables[0])
for direction in all_directions:
    subgroups[f"{direction}"] = {}

if len(tbc.get_names_of_all_directions(tables[0])) == 1:
    lessons = tbc.get_lesson_from_table(tables[0],time_tables[0])
    for lesson in lessons:
        subgroups[f"{all_directions[0]}"][f"{lesson.subject.data_time}"] = lesson.dict()

# elif len(tbc.get_names_of_all_directions(tables[0])) == 2:
#     if tbc.have_groups(tables[0]):

print(subgroups)
