import re
from bs4 import BeautifulSoup, ResultSet, Tag
from IVGU.Table.TableObjects.Constructors import Constructors


class Cell:
    constructors = Constructors()
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
    def __get_teacher_name(teacher_cell: str) -> str:
        teacher = teacher_cell.replace('<','>').split('>')[2].split(',')[0]
        return teacher

    @staticmethod
    def __get_place(teacher_cell:str) ->str:
        place = teacher_cell.replace('<','>').split('>')[2].split(',')[1]
        return place.lstrip()

    def __get_raw_teacher(self,cell: str) -> list[Tag]:
        teacher_cells = BeautifulSoup(cell, 'html.parser').select('.white-space-nowrap')
        clean_teacher_cell = self.__clean_teachers(teacher_cells)
        return clean_teacher_cell

    def __get_first_i(self,tag: Tag):
        return tag.select('i')[0]


    def __clean_teachers(self,teacher_cells:ResultSet[Tag]) -> list[Tag]:
        clean_teachers = []
        for i in teacher_cells:
            clean_teachers.append(self.__get_first_i(i))
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