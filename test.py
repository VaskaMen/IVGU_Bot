from bs4 import BeautifulSoup
import Seecret
from IVGU.Ivgu import Ivgu
from IVGU.TableConvertor import TableConvertor

tbc = TableConvertor()
ivgu = Ivgu()
ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

page = ivgu.get_schedule_page(118, 6, 1, 1, 2)
tables = tbc.get_subject_tables(page)
# print(tables[0])
lines = tbc.get_lines_of_subjects(tables[0])
# print(lines)
new = tbc.lines_separator_into_cells(lines)
for i in new:
    print(i)




# second_tables = BeautifulSoup(page, 'html.parser').select('.second-table')
# second_tables[0].find('thead').extract()
# tr = BeautifulSoup(str(second_tables[0]),'html.parser').select('tr:not(thead tr)')
# td = BeautifulSoup(str(tr[9]),'html.parser').select('td')
# for id,elem in enumerate(td):
#     colspan = elem.get("colspan")
#     if colspan != None:
#         elem["colspan"] = ''
#         for i in range(int(colspan)-1):
#             td.insert(id+i, elem)
#
# for i in td:
#     print(i)





# print(len(tr))
# tables = tbc.get_tables_from_page(page)
# print(tbc.get_groups_names(tables[0]))
# print(tbc.get_quantity_of_subgroups(tables[0]))