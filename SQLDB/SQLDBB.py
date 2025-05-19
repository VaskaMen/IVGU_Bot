from datetime import date, time
from typing import Any

from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule
from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace

from IVGU.ScheduleObject.WorkDay import WorkDay
from SQLDB.SQLEngine import SQLEngine


class SQLDBB(SQLEngine):

    def add_direction_schedule(self,direction: DirectionSchedule, department_id: int, form: int, course: int, level:int):
        direction_id = self.add_direction(direction.direction,department_id)
        id_subdirection = self.add_subdirection(direction.subdirection,direction_id)
        for day in direction.schedule:
            self.add_workday(day,course,level,form,id_subdirection)

    def add_workday(self, workday: WorkDay,course: int, level: int, form: int,id_subdirection: int):
        subgroup = self.add_subgroup(workday.subgroup)
        group = self.add_group(course,subgroup,level,form,id_subdirection)

        workday_db = self.find_last_workday(workday.date, group)
        if workday_db is None:
            workday_id = self.insert_workday(workday.date, group)
            self.add_lessons(workday_id, workday.lessons)
        else:
            workday_id = workday_db[0]
            sql_workday = self.get_workday(workday_id)
            if workday != sql_workday:
                workday_id = self.insert_workday(workday.date, group)
                self.add_lessons(workday_id, workday.lessons)

    def add_lessons(self, workday_id: int, lessons: list[Lesson]):
        for lesson in lessons:
            if str(lesson.name) != 'None':
                lesson_id = self.add_lesson(lesson, workday_id)
                self._add_many_teacher_place(lesson_id, lesson.teacher_places)

    def get_list_institutes(self) -> list[str]:
        list_tuple = self._get_list_institutes()
        return self.__add_any_in_list(list_tuple)

    def get_list_departments(self, institute: str) -> list[str]:
        list_tuple = self._get_list_institute_departments(institute)
        return self.__add_any_in_list(list_tuple)

    def get_list_department_forms(self, department: str) -> list[str]:
        list_tuple = self._get_list_department_forms(department)
        return self.__add_any_in_list(list_tuple)

    def get_list_department_form_levels(self,department: str, form: str):
        list_tuple = self._get_list_department_form_levels(department, form)
        return self.__add_any_in_list(list_tuple)

    def get_list_courses(self, department: str, form: str, level: str):
        list_tuple = self._get_list_courses(department, form, level)
        return self.__add_any_in_list(list_tuple)

    def get_list_directions(self, department: str, form: str, level: str, course: str|int):
        list_tuple = self._get_list_directions(department,form,level,course)
        return self.__add_any_in_list(list_tuple)

    def get_list_subdirections(self, department: str, form: str, level: str, course: str|int, direction: str):
        list_tuple = self._get_list_subdirections(department, form, level, course, direction)
        return self.__add_any_in_list(list_tuple)

    def get_list_subgroups(self, department: str, form: str, level: str, course: str|int, direction: str, subdirection: str):
        list_tuple = self._get_list_subgroups(department, form, level, course, direction,subdirection)
        return self.__add_any_in_list(list_tuple)

    def get_group_id(self, department: str, form: str, level: str, course: str|int, direction: str, subdirection: str, subgroup: str):
        return self._get_group_id(department, form, level, course, direction, subdirection, subgroup)[0]

    def set_user(self, user_id: int, group_id:int, teacher_id: int = 0):
        if self.user_select(user_id) is None:
            self._insert_user(user_id, group_id, teacher_id)
        else:
            self._update_user(user_id, group_id, teacher_id)

    @staticmethod
    def __add_any_in_list(list_of_tuple: list[tuple[Any]]):
        list_of_any = []
        for tuplee in list_of_tuple:
            sm_str = tuplee[0]
            list_of_any.append(sm_str)
        return list_of_any


    def get_workday(self, workday_id):
        date_and_subgroup = self.get_date_and_subgroup_by_workday(workday_id)
        lessons = self.__get_list_lessons(workday_id)

        workday = WorkDay(lessons,date_and_subgroup[0],date_and_subgroup[1])
        return workday

    def __get_list_lessons(self, workday_id: int) -> list[Lesson]:
        lessons = self.get_all_workdays_lessons(workday_id)
        con_lessons = []
        for lesson in lessons:
            lesson_ = self.__lesson_tuple_into_lesson(lesson)
            con_lessons.append(lesson_)
        return con_lessons

    def __lesson_tuple_into_lesson(self, lesson: tuple[time, time, str, str, int]) -> Lesson:
        lesson_id = lesson[4]
        list_teach_place = self.__get_teachers_places(lesson_id)
        time_start = str(lesson[0])[:-3]
        time_start = self.__remove_zero(time_start)
        time_end = str(lesson[1])[:-3]
        time_end = self.__remove_zero(time_end)
        time = time_start + ' ' + '-' + ' ' + time_end
        lesson_ = Lesson(time=time,
                           name=lesson[2],
                           type_subject=lesson[3],
                           teacher_place=list_teach_place)
        return lesson_

    def get_teachers_workday(self, date: date, teacher_id: int) -> WorkDay:
        lessons = self.__get_list_teachers_lessons(date, teacher_id)
        workday = WorkDay(lessons, date, "Belov")
        return workday

    def __get_list_teachers_lessons(self, date: date, teacher_id: int) -> list[Lesson]:
        lessons = self._get_teachers_workday(str(date), teacher_id)
        con_lessons = []
        for lesson in lessons:
            lesson_ = self.__lesson_tuple_into_lesson(lesson)
            con_lessons.append(lesson_)
        return con_lessons


    @staticmethod
    def __remove_zero(elem: str):
        if elem[0] == '0':
            return elem[1:]
        return elem

    def __get_teachers_places(self, lesson_id: int):
        return self.__get_list_teacher_place(self._get_teachers_of_lesson(lesson_id))

    @staticmethod
    def __get_list_teacher_place(teachers) -> list[TeacherPlace]:
        list_teacher_place = []
        for tuple in teachers:
            list_teacher_place.append(TeacherPlace(tuple[0], tuple[1]))
        return list_teacher_place

    def get_actual_dates(self,group_id:int , date: str) -> list[str]:
        dates = self._get_all_dates_after_date(group_id, date)
        return self.__add_any_in_list(dates)

    def get_actual_teacher_dates(self, teacher_id: int, date: str):
        dates = self._get_all_teachers_date_after_date(teacher_id,date)
        return self.__add_any_in_list(dates)