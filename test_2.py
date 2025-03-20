from io import StringIO

import bs4
import pandas as pd
from bs4 import BeautifulSoup

from IVGU.IVGUPage import IVGUPage
from IVGU.Table.TableConvertor import TableConvertor
from IVGU.Table.TableObjects.Cell import Cell

page = IVGUPage("miha2204n@gmail.com","8azr25pb")
tab = TableConvertor()
cel = Cell()

page = page._get_schedule_page(129,6,1,3,2)
tables = tab.get_subject_tables(page)
# strio = StringIO(tables[0])
# table = pd.read_html(strio)
#
# print(table)
# keys = table[0].keys()
# print(keys[2])
#
# g = table[0].get(keys[2])
# for i in g:
#     if not pd.isnull(i):
#         print(i)

bs = BeautifulSoup(tables[0], "html.parser")
all_lessons = bs.select('.less-block .text-bold')
all_teacher_places = bs.select(".white-space-nowrap i")
all_cells = bs.select(".cell")
for lessons in all_lessons:
    lessons.insert_before("$lesson")
    lessons.insert_after("$lesson")
for teachers_place in all_teacher_places:
    teachers_place.insert_before("$teacher")
    teachers_place.insert_after("$teacher")
for cell in all_cells:
    data_time = cel.get_data_time_from_cell(str(cell))
    data_date = cel.get_data_date_from_cell(str(cell))
    cell.insert_before(f"$date_time~{data_time}~")
    cell.insert_after(f"$date_time~{data_time}~")
    cell.insert_before(f"$date_date~{data_date}~")
    cell.insert_after(f"$date_date~{data_date}~")
print(bs.prettify())
# srtio = StringIO(bs.prettify())
# panda = pd.read_html(srtio)
# for i in panda:
#     b = i
#     print(b)

