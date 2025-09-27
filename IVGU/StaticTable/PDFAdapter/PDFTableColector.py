import camelot
from camelot.core import TableList

class PDFTableCollector:
    __tables: TableList
    __weeks = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    def __init__(self, path: str):
        self.__table = self.__read_pdf(path)

    def __read_pdf(self, path: str):
        return camelot.read_pdf(path, pages='all', flavor='lattice', line_scale=40, copy_text=['v', 'h'])

    def get_table_weeks(self):
        pass