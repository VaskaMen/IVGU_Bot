import re
from bs4 import BeautifulSoup, ResultSet, Tag



class Cell:
    def get_subject_name_from_cell(self,cell: str) -> str:
        lesson = self.__get_raw_subject(cell)
        lesson_name = str(lesson[0]).replace('<','>').split('>')[2].split('(')[0]
        return lesson_name

    def get_subject_type_from_cell(self,cell: str) -> str:
        lesson = self.__get_raw_subject(cell)
        type_lesson = str(lesson[0]).replace('<','>').split('>')[2].split('(')[1].replace(")", "")
        return type_lesson

    @staticmethod
    def __get_raw_subject(cell: str) -> ResultSet[Tag]:
        lesson = BeautifulSoup(cell, 'html.parser').select('.text-bold')
        return lesson

    @staticmethod
    def get_teacher_name(teacher_cell: str) -> str:
        teacher = teacher_cell.replace('<','>').split('>')[2].split(',')[0]
        return teacher

    @staticmethod
    def get_place(teacher_cell:str) ->str:
        place = teacher_cell.replace('<','>').split('>')[2].split(',')[1]
        return place.lstrip()

    def get_raw_teacher(self, cell: str) -> list[Tag]:
        teacher_cells = BeautifulSoup(cell, 'html.parser').select('.white-space-nowrap')
        clean_teacher_cell = self.clean_teachers(teacher_cells)
        return clean_teacher_cell

    def get_first_i(self, tag: Tag):
        return tag.select('i')[0]


    def clean_teachers(self, teacher_cells:ResultSet[Tag]) -> list[Tag]:
        clean_teachers = []
        for i in teacher_cells:
            clean_teachers.append(self.get_first_i(i))
        return clean_teachers

    @staticmethod
    def have_digits(string: str) ->bool:
        return len(re.split(r"\d",string)) != 1

    def get_data_date_from_cell(self,cell: str):
        data = self.__get_raw_data(cell)
        return data.get("data-date")

    @staticmethod
    def __get_raw_data(cell: str) -> Tag:
        data = BeautifulSoup(str(cell), 'html.parser').select(".cell")[0]
        return data

    def get_data_time_from_cell(self,cell: str):
        data = self.__get_raw_data(cell)
        return data.get("data-time")

    @staticmethod
    def cells_sorted_by_groups(all_cells: ResultSet[Tag],groups: list[str],have_subgroups:bool) ->dict[str, list[Tag]] :
        sorted_cells: dict[str, list[Tag]] = {}
        if len(groups) == 1:
            sorted_cells[groups[0]] = all_cells
            return sorted_cells
        elif not have_subgroups and len(groups) == 2:
            sorted_cells.setdefault(f'{groups[0]}',[])
            sorted_cells.setdefault(f'{groups[1]}',[])
            for id,cell in enumerate(all_cells):
                sorted_cells[f"{groups[id%2]}"].append(cell)
            return sorted_cells
        elif have_subgroups and len(groups) == 2:
            sorted_cells.setdefault(f'{groups[0]}',[])
            sorted_cells.setdefault(f'{groups[1]}',[])
            counter = 1
            for cell in all_cells:
                if counter == 1 or counter == 2:
                    sorted_cells[f"{groups[0]}"].append(cell)
                if counter == 3 or counter == 4:
                    sorted_cells[f"{groups[1]}"].append(cell)
                if counter == 4:
                    counter = 0
                counter += 1
            return sorted_cells


    def cells_sorted_by_dates(self,all_cells: list[Tag]) ->dict[str, list[Tag]] :
        sorted_cells: dict[str, list[Tag]] = {}
        for cell in all_cells:
            data = self.get_data_date_from_cell(str(cell))
            sorted_cells.setdefault(f"{data}",[])
            sorted_cells[f"{data}"].append(cell)
        return sorted_cells