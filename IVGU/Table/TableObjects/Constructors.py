from bs4 import Tag

from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from IVGU.ScheduleObject.WorkDay import WorkDay
from IVGU.Table.TableObjects.Cell import Cell



class Constructors(Cell):

    def get_teacher_from_cell(self,cell: str) -> list[TeacherPlace]:
        teacher_cell = self.__get_raw_teacher(cell)
        all_teach_place = []
        for i in teacher_cell:
            teacher_place = self.get_teacher_from_tag(i)
            all_teach_place.append(teacher_place)
        return all_teach_place

    def get_teacher_from_tag(self,tag: Tag) ->TeacherPlace:
        teacher = self.__get_teacher_name(str(tag))
        place = self.__get_place(str(tag))
        teach_place = TeacherPlace(teacher,place)
        return teach_place

    def construct_of_subject(self,cell: Tag, subgroup: str,timecodes: dict[str, str]) ->Subject:
        name_of_subject = self.get_subject_name_from_cell(str(cell))
        subject_type = self.get_subject_type_from_cell(str(cell))
        time = timecodes[self.get_data_time_from_cell(str(cell))]
        return Subject(time,name_of_subject,subject_type,subgroup)

    def construct_of_lesson(self,cell: Tag, subgroup: str,timecodes: dict[str, str]) -> Lesson:
        return Lesson(self.construct_of_subject(cell,subgroup,timecodes),self.get_teacher_from_cell(str(cell)))

    def construct_of_empty_lesson(self,cell:Tag, subgroup: str,timecodes: dict[str, str]) ->Lesson:
        return Lesson(self.construct_of_empty_subject(cell,subgroup,timecodes),list())

    def construct_of_empty_subject(self,cell:Tag, subgroup: str,timecodes: dict[str, str]) ->Subject:
        time = timecodes[self.get_data_time_from_cell(str(cell))]
        return Subject(time=time,group=subgroup)

    def construct_of_workday(self,cell:Tag,lessons:list[Lesson]):
        data = self.get_data_date_from_cell(str(cell))
        return WorkDay(lessons,data)