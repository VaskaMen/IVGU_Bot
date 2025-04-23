from io import StringIO

import pandas as pd

from IVGU.IVGUPage import IVGUPage
from IVGU.Table.NewTableConvertor import NewTableConvertor
from IVGU.Table.TableMarkup import TableMarkup
from IVGU.Table.TableObjects.Cell import Cell
from IVGU.Table.TableExtractor import TableExtractor

page = IVGUPage("miha2204n@gmail.com","8azr25pb")
cel = Cell()
newtab = NewTableConvertor()
tableex = TableExtractor()

page = page._get_schedule_page(129,6,1,3,2)
tables = tableex.get_subject_tables(page)
tbmark = TableMarkup(str(tables[0]))
tbmark.table_markup()



time_table = tableex.get_time_table(page)
timecodes = newtab.get_time_codes(time_table)

print(tbmark.table.prettify())
srtio = StringIO(tbmark.table.prettify())
panda = pd.read_html(srtio)
keys = panda[0].keys()
lines = panda[0].get(keys[1])

all_subgroups = newtab.get_all_subgroups(keys)
for key in keys:
    for line in lines:
        if not pd.isnull(line):
           print(newtab.get_subject(timecodes,newtab.get_subgroup(key), line))



st1 = "$date_time~13~  $date_date~2025-04-26~  $lesson  Английский язык в сфере профессиональной коммуникации (практическое занятие)  (Факультатив)  $lesson  $teacher  Доцент Мелентьева О.А., Д - Дистанционно  $teacher  $teacher  Доцент Москалева С.И., Д - Дистанционно  $teacher  $date_date~2025-04-26~  $date_time~13~"
print(newtab.get_lesson(timecodes,"EA",st1))

# for teachplace in all_teahplaces:
#     print(newtab.get_teacher(teachplace))
#     print(newtab.get_place(teachplace))
#     print("")

