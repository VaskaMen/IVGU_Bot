from datetime import date, datetime

from pandas import Index, DataFrame

from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule
from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from IVGU.ScheduleObject.WorkDay import WorkDay
from IVGU.Table.LineConvertor import LineConvertor


class Constructors(LineConvertor):
    def get_lesson(self, timecodes:dict[str,str], line:str) ->Lesson:
        time = self._get_time(line, timecodes)
        name = self._get_name_of_lesson(line)
        type_subject = self._get_type_of_subject(line)
        teacher_place = self.get_list_of_teacherplace(line)
        return Lesson(
            time= time,
            name=name,
            type_subject=type_subject,
            teacher_place=teacher_place
        )

    def get_lessons(self, timecodes:dict[str,str], lines: list[str]) ->list[Lesson]:
        all_lessons = []
        for line in lines:
            lesson = self.get_lesson(timecodes,line)
            all_lessons.append(lesson)
        return all_lessons

    def get_list_of_teacherplace(self,line: str):
        all_teacherplaces = []
        all_teachers_with_place = self.get_teachers_with_place(line)
        for teachers_with_place in  all_teachers_with_place:
            all_teacherplaces.append(self.get_teacherplace(teachers_with_place))
        return all_teacherplaces

    def get_teacherplace(self, teacherplace: str) -> TeacherPlace:
        teacher = self.get_teacher(teacherplace)
        place = self.get_place(teacherplace)
        return TeacherPlace(teacher,place)

    def get_workdays(self,timecodes:dict[str,str], subgroup: str, sorted_lines:dict[str, list[str]]) -> list[WorkDay]:
        list_workdays = []
        for date in sorted_lines:
            lessons = self.get_lessons(timecodes,sorted_lines[date])
            workday = WorkDay(lessons = lessons,date = self.converted_day(date),subgroup = subgroup)
            list_workdays.append(workday)
        return list_workdays

    @staticmethod
    def converted_day(raw_date:str) -> date:
        converted_date = datetime.strptime(raw_date,'%Y-%m-%d').date()
        return converted_date

    def get_direction_schedules(self, timecodes:dict[str,str],table: DataFrame) -> list[DirectionSchedule]:
        tablehadders:Index = table.keys()
        list_direction_schedule = []
        for tablehead in tablehadders:
            lines = table.get(tablehead)
            sorted_lines = self.lines_sorted_by_dates(lines)
            workdays = self.get_workdays(timecodes,self.get_subgroup(tablehead),sorted_lines)
            direction_schedule = DirectionSchedule(self.get_subdirection(tablehead),workdays)
            list_direction_schedule.append(direction_schedule)
        return list_direction_schedule

    def get_all_subgroups(self, keys_subgroups: Index) -> list[str]:
        all_subgroups = []
        for key in keys_subgroups:
            all_subgroups.append(self.get_subgroup(key))
        return all_subgroups

    @staticmethod
    def get_subgroup(key_subgroup) -> str:
        return key_subgroup[-1]

    @staticmethod
    def get_subdirection(key_subgroup) -> str:
        return key_subgroup[1]