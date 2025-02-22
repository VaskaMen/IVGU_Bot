import re

from bs4 import BeautifulSoup, ResultSet, Tag

from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace


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

    def get_teacher_from_cell(self,cell: str) -> list[TeacherPlace]:
        teacher_cell = self.__get_raw_teacher(cell)
        all_teach_place = []
        for i in teacher_cell:
            teacher = self.__get_teacher_name(str(i))
            place = self.__get_place(str(i))
            teach_place = TeacherPlace(teacher,place)
            all_teach_place.append(teach_place)
        return all_teach_place

    @staticmethod
    def __get_teacher_name(teacher_cell: str):
        teacher = teacher_cell.replace('<','>').split('>')[2].split(',')[0]
        return teacher

    @staticmethod
    def __get_place(teacher_cell:str):
        place = teacher_cell.replace('<','>').split('>')[2].split(',')[1]
        return place.lstrip()

    def __get_raw_teacher(self,cell: str) -> list[Tag]:
        teacher_cell = BeautifulSoup(cell, 'html.parser').select('.white-space-nowrap i')
        clean_teacher_cell = self.__clean_teachers(teacher_cell)
        return clean_teacher_cell

    def __clean_teachers(self,teacher_cells:ResultSet[Tag]) -> list[Tag]:
        clean_teachers = []
        for i in teacher_cells:
            if self.have_digits(i.text):
                clean_teachers.append(i)
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
        data = data = self.__get_raw_data(cell)
        return data.get("data-time")

    def construct_of_subject(self,cell: Tag, subgroup: str,timecodes: dict[str, str]) ->Subject:
        name_of_subject = self.get_subject_name_from_cell(str(cell))
        subject_type = self.get_subject_type_from_cell(str(cell))
        time = timecodes[self.get_data_time_from_cell(str(cell))]
        return Subject(time,name_of_subject,subject_type,subgroup)

    def construct_of_lesson(self,cell: Tag, subgroup: str,timecodes: dict[str, str]) -> Lesson:
        return Lesson(self.construct_of_subject(cell,subgroup,timecodes),self.get_teacher_from_cell(str(cell)))
