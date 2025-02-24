from bs4 import BeautifulSoup
from rich.console import Console
import Seecret
from IVGU.Ivgu import Ivgu
from IVGU.Table.TableConvertor import TableConvertor
tbc = TableConvertor()
ivgu = Ivgu()
console = Console()
ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

page = ivgu.get_schedule_page(118, 6, 1, 1, 2)
tables = tbc.get_subject_tables(page)
time_tables = tbc.get_time_table(page)




lessons = tbc.get_workdays_from_table(tables[0],time_tables[0])


subgroups = {}
all_directions = tbc.get_names_of_all_directions(tables[0])

console.print(lessons)