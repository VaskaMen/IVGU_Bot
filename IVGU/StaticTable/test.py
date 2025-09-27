import camelot
from camelot.core import Table

from IVGU.StaticTable.StaticIVGU import StaticIVGU

#
# i = StaticIVGU()
# # i.download_all_schedules()


tables = camelot.read_pdf(f'schedule/schedule_32.pdf', pages='all', flavor='lattice',  line_scale=40, copy_text=['v', 'h'])
table: Table = tables[0]
table_data = []

for i in table.data:
    if i[0] in weeks:
        table_data.append(i)

for i in table_data:
    print(i)
