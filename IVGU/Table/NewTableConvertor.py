from datetime import date, datetime

from bs4 import BeautifulSoup, ResultSet, PageElement, Tag, NavigableString
from pandas import Index

from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from IVGU.ScheduleObject.WorkDay import WorkDay
from IVGU.Table.LineConvertor import LineConvertor


class NewTableConvertor(LineConvertor):
    def get_subject(self,timecodes:dict[str,str], subgroup: str,line:str) -> Subject:
        time = self._get_time(line, timecodes)
        name = self._get_name_of_lesson(line)
        type = self._get_type_of_subject(line)
        return Subject(time,name,type,subgroup)

    @staticmethod
    def __result_set_to_list_str(result_set:  ResultSet[PageElement | Tag | NavigableString]) -> list[str]:
        mas = []
        for result in result_set:
            mas.append(str(result))
        return mas

    @staticmethod
    def get_time_codes(tbody:ResultSet[Tag]) -> dict[str,str]:
        all_times = BeautifulSoup(str(tbody), "html.parser").select('.text-bold.cell.text-center')
        time_codes = {}
        for i in all_times:
            time_codes[f"{i.get('data-time')}"] = i.text
        return time_codes

    @staticmethod
    def get_all_subgroups(keys_subgroups: Index) -> list[str]:
        all_subgroups = []
        for key in keys_subgroups:
            all_subgroups.append(key[-1])
        return all_subgroups

    @staticmethod
    def get_subgroup(key_subgroup) -> str:
        return key_subgroup[-1]

    def get_teacherplace(self, teacherplace: str) -> TeacherPlace:
        teacher = self.get_teacher(teacherplace)
        place = self.get_place(teacherplace)
        return TeacherPlace(teacher,place)

    def get_list_of_teacherplace(self,line: str):
        all_teacherplaces = []
        all_teachers_with_place = self.get_teachers_with_place(line)
        for teachers_with_place in  all_teachers_with_place:
            all_teacherplaces.append(self.get_teacherplace(teachers_with_place))
        return all_teacherplaces

    def get_lesson(self, timecodes:dict[str,str], subgroup: str,line:str) ->Lesson:
        return Lesson(self.get_subject(timecodes,subgroup,line),self.get_list_of_teacherplace(line))

    def get_lessons(self, timecodes:dict[str,str], subgroup: str, lines: list[str]) ->list[Lesson]:
        all_lessons = []
        for line in lines:
            lesson = self.get_lesson(timecodes,subgroup,line)
            all_lessons.append(lesson)
        return all_lessons

    @staticmethod
    def converted_day(raw_date:str) -> date:
        converted_date = datetime.strptime(raw_date,'%Y-%m-%d').date()
        return converted_date

    def get_workdays(self,timecodes:dict[str,str], subgroup: str, sorted_lines:dict[str, list[str]]) -> list[WorkDay]:
        list_workdays = []
        for date in sorted_lines:
            lessons = self.get_lessons(timecodes, subgroup,sorted_lines[date])
            workday = WorkDay(lessons,self.converted_day(date))
            list_workdays.append(workday)
        return list_workdays