from io import StringIO

import bs4
import pandas as pd
from bs4 import BeautifulSoup

from IVGU.IVGUPage import IVGUPage
from IVGU.Table.TableConvertor import TableConvertor
from IVGU.Table.TableMarkup import TableMarkup
from IVGU.Table.TableObjects.Cell import Cell

page = IVGUPage("miha2204n@gmail.com","8azr25pb")
tab = TableConvertor()
cel = Cell()

page = page._get_schedule_page(129,6,1,3,2)
tables = tab.get_subject_tables(page)
tbmark = TableMarkup(tables[0])
tbmark.table_markup()
# strio = StringIO(tables[0])
# table = pd.read_html(strio)
#
# print(table)






# print(tbmark.table.prettify())
srtio = StringIO(tbmark.table.prettify())
panda = pd.read_html(srtio)
keys = panda[0].keys()
lines = panda[0].get(keys[2])
for line in lines:
    if not pd.isnull(line):
        print(line)

