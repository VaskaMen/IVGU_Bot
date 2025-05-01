from IVGU.IVGUPage import IVGUPage
from IVGU.Table.Table import Table

page = IVGUPage("miha2204n@gmail.com","8azr25pb")
tbl = Table()
page = page._get_schedule_page(129,6,1,3,2)
sch = tbl.get_schedules(page)
for sc in sch:
    print(sc)