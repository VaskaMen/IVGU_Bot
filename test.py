from bs4 import BeautifulSoup
import Seecret
from IVGU.Ivgu import Ivgu
from IVGU.Table.TableConvertor import TableConvertor
tbc = TableConvertor()
ivgu = Ivgu()
ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

page = ivgu.get_schedule_page(118, 6, 1, 1, 2)
tables = tbc.get_subject_tables(page)
lines = tbc.line.get_lines_of_subjects(tables[0])
new = tbc.line.lines_separator_into_cells(lines)

time_tables = tbc.get_time_table(page)
tbody = tbc.get_tbody_of_times(time_tables[1])
timecodes = tbc.get_time_codes(tbody)
quantity = tbc.get_quantity_of_subgroups(tables[0])

for i in new:
    if i.text != "":
        print(tbc.cell.get_subject_name_from_cell(str(i)))
        print(tbc.cell.get_subject_type_from_cell(str(i)))
        print(tbc.cell.get_teacher_from_cell(str(i)))
        print(tbc.cell.get_data_date_from_cell(str(i)))
        print(timecodes[tbc.cell.get_data_time_from_cell(str(i))])
        print("")






# ivgu = Ivgu()

# page = ivgu.get_schedule_page(118, 6, 1, 1, 2)
