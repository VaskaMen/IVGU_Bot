from typing import Any

from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule

from IVGU.ScheduleObject.WorkDay import WorkDay
from SQLDB.SQLEngine import SQLEngine
from SQLDB.SQLLesson import SQLLesson
from SQLDB.SQLTeacherPlace import SQLTeacherPlace


class SQLDBB(SQLEngine):

    def add_direction_schedule(self,direction: DirectionSchedule, department_id: int, form: int, course: int, level:int):
        direction_id = self.add_direction(direction.direction,department_id)
        id_subdirection = self.add_subdirection(direction.subdirection,direction_id)
        for day in direction.schedule:
            self.add_workday(day,course,level,form,id_subdirection)

    def add_workday(self, workday: WorkDay,course: int, level: int, form: int,id_subdirection: int):
        subgroup = self.add_subgroup(workday.subgroup)
        group = self.add_group(course,subgroup,level,form,id_subdirection)
        for lesson in workday.lessons:
            if str(lesson.name) != 'None':
                lesson_id = self.add_lesson(lesson, workday.date, group)
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

    def set_user(self, user_id: int, group_id:int):
        if self.user_select(user_id) is None:
            self._insert_user(user_id, group_id)
        else:
            self._update_user(user_id, group_id)

    @staticmethod
    def __add_any_in_list(list_of_tuple: list[tuple[Any]]):
        list_of_any = []
        for tuplee in list_of_tuple:
            sm_str = tuplee[0]
            list_of_any.append(sm_str)
        return list_of_any

    def get_sql_workday(self, date: str, group_id: int, lesson_id: int):
        workday = self.get_workday(group_id, date)
        list_teach_place = self.get_list_teacher_place(self.get_teachers_of_lesson(lesson_id))
        sqlworkday = []
        for lesson in workday:
             sqllesson = SQLLesson(subject_name=lesson[0],
                      time_start=lesson[1],
                      time_end=lesson[2],
                      type_name=lesson[3],
                      date=lesson[4],
                      teach_places=list_teach_place)
             sqlworkday.append(sqllesson)
        return sqlworkday

    @staticmethod
    def get_list_teacher_place(teachers) -> list[SQLTeacherPlace]:
        list_teacher_place = []
        for tuple in teachers:
           list_teacher_place.append(SQLTeacherPlace(tuple[0], tuple[1]))
        return list_teacher_place