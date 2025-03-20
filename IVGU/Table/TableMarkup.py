from bs4 import Tag, BeautifulSoup

from IVGU.Table.TableObjects.Cell import Cell


class TableMarkup:
    cel = Cell()
    def __init__(self, table:str):
        self.table = BeautifulSoup(table, "html.parser")

    def table_markup(self):
        self.__add_indicator_of_subject()
        self.__add_indicator_of_teacher_place()
        self.__add_indicator_of_cell()

    def __add_indicator_of_subject(self):
        all_lessons = self.table.select('.less-block .text-bold')
        for lessons in all_lessons:
            self.__insert_indicator_around(lessons, "$lesson")

    def __add_indicator_of_teacher_place(self):
        all_teacher_places = self.table.select(".white-space-nowrap i")
        for teachers_place in all_teacher_places:
            self.__insert_indicator_around(teachers_place, "$teacher")

    def __add_indicator_of_cell(self):
        all_cells = self.table.select(".cell")
        for cell in all_cells:
            self.__add_indicator_of_data_time(cell)
            self.__add_indicator_of_data_date(cell)

    def __add_indicator_of_data_time(self, cell:Tag):
        data_time = self.cel.get_data_time_from_cell(str(cell))
        self.__insert_indicator_around(cell,f"$date_time~{data_time}~")

    def __add_indicator_of_data_date(self, cell:Tag):
        data_date = self.cel.get_data_date_from_cell(str(cell))
        self.__insert_indicator_around(cell,f"$date_date~{data_date}~")

    @staticmethod
    def __insert_indicator_around(lessons: Tag, indicator: str):
        lessons.insert_before(indicator)
        lessons.insert_after(indicator)