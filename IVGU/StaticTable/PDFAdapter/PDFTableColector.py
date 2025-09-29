import camelot
from camelot.core import TableList, Table


class PDFTableCollector:
    __tables: TableList
    __weeks = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    __data: list[list[str]] = list()

    def __init__(self, path: str):
        self.__tables = self.__read_pdf(path)
        self.__extract_data()

    def __read_pdf(self, path: str):
        return camelot.read_pdf(path, pages='all', flavor='lattice', line_scale=40, copy_text=['v', 'h'])

    def __extract_data(self):
        for table in self.__tables:
            self.__extract_table_data(table)

    def __extract_table_data(self, table: Table):
        data = table.data
        for line in data:
            self.__append_table_data(line)

    def __append_table_data(self, data: list[str]):
        if data[0] in self.__weeks:
            self.__data.append(data)

    def __count_max_columns(self):
        max = 0
        for i in self.__data:
            if len(i) > max:
                max = len(i)
        return max
