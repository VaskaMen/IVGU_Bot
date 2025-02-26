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




workdays = tbc.get_lessons_from_table(tables[0],time_tables[0])

console.print(workdays)