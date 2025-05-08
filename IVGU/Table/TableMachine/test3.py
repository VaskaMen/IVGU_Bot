from io import StringIO

from IVGU.APIIVGU import APIIVGU
from IVGU.Table.TableMachine.TableExtractor import TableExtractor
from IVGU.Table.TableMachine.TableMarkup import TableMarkup
import pandas as pd
api = APIIVGU("miha2204n@gmail.com","8azr25pb")


link = "/info/showschedule/126/6/1/2/2"

page = api.get_page(link)
tables = TableExtractor().get_subject_tables(page)
mark = TableMarkup(str(tables[0]))
markup = mark.table_markup()
srtio = StringIO(mark.table.prettify())
panda = pd.read_html(srtio)
print(panda)
