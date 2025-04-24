from io import StringIO

import pandas as pd

from IVGU.IVGUPage import IVGUPage
from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule
from IVGU.ScheduleObject.WorkDay import WorkDay
from IVGU.Table.NewTableConvertor import NewTableConvertor
from IVGU.Table.TableMarkup import TableMarkup
from IVGU.Table.TableObjects.Cell import Cell
from IVGU.Table.TableExtractor import TableExtractor

page = IVGUPage("miha2204n@gmail.com","8azr25pb")
cel = Cell()
newtab = NewTableConvertor()
tableex = TableExtractor()
page = page._get_schedule_page(118,6,1,1,2)
tables = tableex.get_subject_tables(page)
tbmark = TableMarkup(str(tables[0]))
tbmark.table_markup()



time_table = tableex.get_time_table(page)
timecodes = newtab.get_time_codes(time_table)

srtio = StringIO(tbmark.table.prettify())
panda = pd.read_html(srtio)
keys = panda[0].keys()
lines = panda[0].get(keys[2])
sorted_lines = newtab.lines_sorted_by_dates(lines)

all_subgroups = newtab.get_all_subgroups(keys)
all_directions = newtab.get_all_directions(keys)
for key in keys:
    workdays = newtab.get_workdays(timecodes,newtab.get_subgroup(key), sorted_lines)
    for workday in workdays:
        print(workday)


# workdays = newtab.get_workdays(timecodes,newtab.get_subgroup(keys[2]), sorted_lines)
# for workday in workdays:
#     print(workday)