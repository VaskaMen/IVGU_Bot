from bs4 import BeautifulSoup, ResultSet, Tag


class Cell:
    def get_subject_name_from_cell(self,cell: str) -> str:
        lesson = self.get_raw_subject(cell)
        lesson_name = str(lesson[0]).replace('<','>').split('>')[2].split('(')[0]
        return lesson_name

    def get_subject_type_from_cell(self,cell: str) -> str:
        lesson = self.get_raw_subject(cell)
        type_lesson = str(lesson[0]).replace('<','>').split('>')[2].split('(')[1].replace(")", "")
        return type_lesson

    @staticmethod
    def get_raw_subject(cell: str) -> ResultSet[Tag]:
        lesson = BeautifulSoup(cell, 'html.parser').select('.text-bold')
        return lesson

    def get_teacher_from_cell(self,cell: str) -> str:
        teacher_cell = self.get_raw_teacher(cell)
        teacher = str(teacher_cell[0]).replace('<','>').split('>')[2].split(',')[0]
        return teacher

    @staticmethod
    def get_raw_teacher(cell: str) -> ResultSet[Tag]:
        teacher_cell = BeautifulSoup(cell, 'html.parser').select('.white-space-nowrap i')
        return teacher_cell

    def get_place_from_cell(self,cell: str) -> str:
        place_cell = self.get_raw_teacher(cell)
        place = str(place_cell[0]).replace('<','>').split('>')[2].split(',')[1].lstrip()
        return place

    def get_data_date_from_cell(self,cell: str):
        data = self.get_raw_data(cell)
        return data.get("data-date")

    @staticmethod
    def get_raw_data(cell: str):
        data = BeautifulSoup(str(cell), 'html.parser').select(".cell")[0]
        return data

    def get_data_time_from_cell(self,cell: str):
        data = data = self.get_raw_data(cell)
        return data.get("data-time")