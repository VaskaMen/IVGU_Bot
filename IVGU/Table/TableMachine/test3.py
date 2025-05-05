from IVGU.APIIVGU import APIIVGU
from IVGU.Table.TableMachine.TableExtractor import TableExtractor
from IVGU.Table.TableMachine.TableMarkup import TableMarkup

api = APIIVGU("miha2204n@gmail.com","8azr25pb")


link = "/info/showschedule/126/6/1/2/2"

page = api.get_page(link)
tables = TableExtractor().get_subject_tables(page)
mark = TableMarkup(str(tables[0]))
markup = mark.table_markup()
tbl = mark.table.prettify()
print(tbl)
