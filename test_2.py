from io import StringIO

import pandas as pd

from IVGU.IVGUPage import IVGUPage
from IVGU.Table.TableConvertor import TableConvertor
from IVGU.Table.TableMarkup import TableMarkup

from IVGU.Table.TableObjects.Cell import Cell
from IVGU.Table.TableExtractor import TableExtractor

page = IVGUPage("miha2204n@gmail.com","8azr25pb")
cel = Cell()
tbc = TableConvertor()
tableex = TableExtractor()
page = page._get_schedule_page(129,6,1,3,2)
tables = tableex.get_subject_tables(page)


modifided_table = tbc.split_directions(str(tables[0]))

tbmark = TableMarkup(str(modifided_table))
tbmark.table_markup()

time_table = tableex.get_time_table(page)
timecodes = tableex.get_time_codes(time_table)

srtio = StringIO(tbmark.table.prettify())
panda = pd.read_html(srtio)

direction_schedules = tbc.get_direction_schedules(timecodes, panda[0])
for dir in direction_schedules:
    print(dir)