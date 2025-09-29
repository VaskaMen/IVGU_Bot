import camelot
from camelot.core import Table, TableList

from IVGU.StaticTable.PDFAdapter.PDFTableColector import PDFTableCollector
from IVGU.StaticTable.StaticIVGU import StaticIVGU

#
# i = StaticIVGU()
# # i.download_all_schedules()


tables: TableList = camelot.read_pdf(f'schedule/schedule_0.pdf', pages='all', flavor='lattice',  line_scale=40, copy_text=['v', 'h'])
r: Table = tables[0]

r.to_html("h.html")

# a = PDFTableCollector("schedule/schedule_0.pdf")
# print(a)
