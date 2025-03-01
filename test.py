from adodbapi.ado_consts import directions
from bs4 import BeautifulSoup
from rich.console import Console
import Seecret
from IVGU.Ivgu import Ivgu
from IVGU.Table.TableConvertor import TableConvertor
from JsonDB.WorkDaysDB import WorkDaysDB

tbc = TableConvertor()
ivgu = Ivgu()
console = Console()
wddb = WorkDaysDB("luboe.json")

ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

page = ivgu.get_schedule_page(118, 6, 1, 1, 2)
tables = tbc.get_subject_tables(page)
time_tables = tbc.get_time_table(page)
directions = tbc.get_names_of_all_directions(tables[0])



lessons_sorted = tbc.get_direction_schedule(tables[1],time_tables[1])
wddb.add_directions_schedule(lessons_sorted)
# console.print(lessons_sorted[0].dict())