from typing import Any

import psycopg2
from psycopg2._psycopg import connection

from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from SQLDB.SQLCommands.CreateCommands import CreateCommands
from SQLDB.SQLCommands.SQLCommands import SQLCommands
from datetime import datetime


class SQLEngine:
    __con: connection | connection = None

    def __init__(self):
        self.connect()
        self.__con.autocommit = True

        self.__cur = self.__con.cursor()
        self.__cur.execute(CreateCommands.create_table_levels())
        self.__cur.execute(CreateCommands.create_table_institutes())
        self.__cur.execute(CreateCommands.create_table_departments())
        self.__cur.execute(CreateCommands.create_table_forms())
        self.__cur.execute(CreateCommands.create_table_groups())
        self.__cur.execute(CreateCommands.create_table_places())
        self.__cur.execute(CreateCommands.create_table_lessons())
        self.__cur.execute(CreateCommands.create_table_directions())
        self.__cur.execute(CreateCommands.create_table_subdirections())
        self.__cur.execute(CreateCommands.create_table_subgroups())
        self.__cur.execute(CreateCommands.create_table_subjects())
        self.__cur.execute(CreateCommands.create_table_teachers())
        self.__cur.execute(CreateCommands.create_table_teachers_lesson())
        self.__cur.execute(CreateCommands.create_table_types())
        self.__cur.execute(CreateCommands.create_table_users())
        self.__cur.execute(CreateCommands.create_table_workday())
        self.__con.commit()
        self.__cur.execute(SQLCommands.add_level(1,"Бакалавриат"))
        self.__cur.execute(SQLCommands.add_level(2,"Магистратура"))
        self.__cur.execute(SQLCommands.add_level(3,"Специалитет"))
        self.__cur.execute(SQLCommands.add_level(4,"ДОП"))
        self.__cur.execute(SQLCommands.add_form(6,'Очная Форма обучения'))
        self.__cur.execute(SQLCommands.add_form(8,'Очно-заочная Форма обучения'))
        self.__cur.execute(SQLCommands.add_form(7,'Заочная Форма обучения'))
        self.__cur.execute(SQLCommands.add_group(-1,-1,-1,-1,-1))

    def connect(self):
        self.__con = psycopg2.connect(
            host="localhost",
            database="Ivgu",
            user="postgres",
            password="admin",
            port=5432,
            client_encoding='UTF-8',


        )

    def close_connection(self):
        self.__con.close()

    def _add_subject(self, lesson: Lesson) -> int:
        self.__cur.execute(SQLCommands.add_subject(lesson.name))
        self.__cur.execute(SQLCommands.find_subject_id_by_name(lesson.name))
        return  self.__cur.fetchone()[0]

    def _add_teacher_place(self, lesson_id: int, teacher_place: TeacherPlace):
        place = self.add_place(teacher_place)
        teacher = self._add_teacher(teacher_place)
        self.__cur.execute(SQLCommands.add_teachers_of_lesson(teacher, lesson_id, place))

    def _add_many_teacher_place(self, lesson_id: int, many_teacher_places: list[TeacherPlace]):
        for teacher_place in many_teacher_places:
            self._add_teacher_place(lesson_id, teacher_place)

    def _add_teacher(self, teachplace: TeacherPlace) -> int:
        self.__cur.execute(SQLCommands.add_teacher(teachplace.teacher))
        self.__cur.execute(SQLCommands.find_id_teacher(teachplace.teacher))
        return self.__cur.fetchone()[0]

    def add_place(self, teachplace: TeacherPlace) -> int:
        self.__cur.execute(SQLCommands.add_place(teachplace.place))
        self.__cur.execute(SQLCommands.find_place_id(teachplace.place))
        return self.__cur.fetchone()[0]

    def add_subgroup(self, subgroup_name: str):
        self.__cur.execute(SQLCommands.add_subgroup(subgroup_name))
        self.__cur.execute(SQLCommands.find_id_subgroup(subgroup_name))
        return self.__cur.fetchone()[0]

    def add_direction(self, direction: str, department_id: int):
        self.__cur.execute(SQLCommands.add_direction(direction, department_id))
        self.__cur.execute(SQLCommands.find_direction_id(direction,department_id))
        return self.__cur.fetchone()[0]

    def add_subdirection(self, subdirection: str, direction_id: int):
        self.__cur.execute((SQLCommands.add_subdirection(subdirection, direction_id)))
        self.__cur.execute(SQLCommands.find_subdirection_id(subdirection,direction_id))
        return self.__cur.fetchone()[0]

    def add_department(self, id_of_department: int, name: str, id_of_institute: int):
        self.__cur.execute(SQLCommands.add_department(id_of_department, name, id_of_institute))

    def add_institute(self, id_of_institute: int, name: str):
        self.__cur.execute(SQLCommands.add_institute(id_of_institute, name))

    def add_lesson(self, lesson: Lesson, workday: int):
        subject = self._add_subject(lesson)
        type_for_lesson = self.add_type(lesson.type_subject)
        lesson_time = lesson.time
        start_time = self.__get_start_time(lesson_time)
        end_time = self.__get_end_time(lesson_time)
        self.__cur.execute(SQLCommands.add_lesson(subject, start_time, end_time, type_for_lesson, workday))
        self.__cur.execute(SQLCommands.find_id_lesson(subject, start_time, end_time, type_for_lesson, workday))
        return self.__cur.fetchone()[0]


    def __get_start_time(self,time: str):
        return self.__time_slicer(time,0)

    def __get_end_time(self,time: str):
       return self.__time_slicer(time,1)

    @staticmethod
    def __time_slicer(time: str, cif: int) -> str:
        null = "0"
        time_sliced = time.split("-")[cif].strip()
        if len(time_sliced) < 5:
            con = null + time_sliced
            return con
        else:
            return time_sliced

    def add_group(self, course: int, subgroup: int, level: int,form: int, subdirection: int):
        self.__cur.execute(SQLCommands.add_group(course, subgroup, level, form, subdirection))
        self.__cur.execute(SQLCommands.find_id_group(course, subgroup, level, form, subdirection))
        return self.__cur.fetchone()[0]

    def add_type(self, name: str) -> int:
        self.__cur.execute(SQLCommands.add_type(name))
        self.__cur.execute(SQLCommands.find_type_id_by_name(name))
        return self.__cur.fetchone()[0]

    def _get_list_institutes(self) -> list[tuple[Any, ...]]:
        self.__cur.execute(SQLCommands.select_all_institutes())
        return self.__cur.fetchall()

    def _get_list_institute_departments(self, institute: str):
        self.__cur.execute(SQLCommands.select_all_institute_departments(institute))
        return self.__cur.fetchall()

    def _get_list_department_forms(self, department: str):
        self.__cur.execute(SQLCommands.select_all_department_forms(department))
        return self.__cur.fetchall()

    def _get_list_department_form_levels(self,department: str, form: str):
        self.__cur.execute(SQLCommands.select_all_department_form_levels(department,form))
        return self.__cur.fetchall()

    def _get_list_courses(self, department: str, form: str, level: str):
        self.__cur.execute(SQLCommands.select_all_courses(department,form,level))
        return self.__cur.fetchall()

    def _get_list_directions(self, department: str, form: str, level: str, course: str|int):
        self.__cur.execute(SQLCommands.get_directions(department, form, level, course))
        return self.__cur.fetchall()

    def _get_list_subdirections(self, department: str, form: str, level: str, course: str|int, direction: str):
        self.__cur.execute(SQLCommands.get_subdirections(department, form, level, course, direction))
        return self.__cur.fetchall()

    def _get_list_subgroups(self, department: str, form: str, level: str, course: str|int, direction: str, subdirection: str):
        self.__cur.execute(SQLCommands.get_subgroups(department, form, level, course, direction, subdirection))
        return self.__cur.fetchall()

    def _get_group_id(self, department: str, form: str, level: str, course: str|int, direction: str, subdirection: str, subgroup: str):
        self.__cur.execute(SQLCommands.get_group_id(department, form, level, course, direction, subdirection,subgroup))
        return self.__cur.fetchone()

    def _insert_user(self, user_id: int, group_id: int, teacher_id: int = 0):
        return self.__cur.execute(SQLCommands.insert_user(user_id, group_id, teacher_id))

    def _update_user(self, user_id: int, group_id: int, teacher_id: int = 0):
        self.__cur.execute(SQLCommands.update_user(user_id, group_id, teacher_id))

    def update_schedule_user(self, update: bool, user_id: int):
        self.__cur.execute(SQLCommands.update_schedule_user(update,user_id))

    def user_select(self, user_id: int):
        self.__cur.execute(SQLCommands.user_select(user_id))
        return self.__cur.fetchone()

    def _get_teachers_workday(self, date: str,teachers_id: int):
        self.__cur.execute(SQLCommands.get_teachers_workday(date,teachers_id))
        return self.__cur.fetchall()

    def _get_teachers_of_lesson(self, lesson_id: int):
        self.__cur.execute(SQLCommands.get_teachers_of_lesson(lesson_id))
        return self.__cur.fetchall()

    def _get_all_dates_after_date(self,group_id: int, date: str):
        self.__cur.execute(SQLCommands.get_dates_after_date(group_id, date))
        return self.__cur.fetchall()

    def _get_all_teachers_date_after_date(self, teacher_id: int, date: str):
        self.__cur.execute(SQLCommands.get_teacher_dates_after_date(teacher_id,date))
        return self.__cur.fetchall()

    def get_teacher_id(self, teacher_name: str):
        self.__cur.execute(SQLCommands.find_teacher_id_by_name(teacher_name))
        return self.__cur.fetchone()

    def get_teachers_group(self):
        self.__cur.execute(SQLCommands.find_teachers_group())
        return self.__cur.fetchone()

    def get_users_teacher_id(self, user_id: int):
        self.__cur.execute(SQLCommands.find_user_teacher_id(user_id))
        return self.__cur.fetchone()

    def update_if_teach_to_student(self, user_id: int):
        self.__cur.execute(SQLCommands.update_if_teach_to_student(user_id))

    def insert_workday(self, date: datetime.date, group_id: int):
        self.__cur.execute(SQLCommands.add_workday(date, group_id))
        self.__cur.execute(SQLCommands.find_last_workday(date, group_id))
        return self.__cur.fetchone()[0]

    def find_last_workday(self, date: datetime.date, group_id: int):
        self.__cur.execute(SQLCommands.find_last_workday(date, group_id))
        return self.__cur.fetchone()

    def get_all_workdays_lessons(self, workday_id: int):
        self.__cur.execute(SQLCommands.find_workday_lessons(workday_id))
        return self.__cur.fetchall()

    def get_date_and_subgroup_by_workday(self, workday_id: int):
        self.__cur.execute(SQLCommands.get_date_subgroup_by_workday(workday_id))
        return self.__cur.fetchone()

    def get_last_insert_date_workday(self) -> datetime:
        self.__cur.execute(SQLCommands.get_last_insert_date_workday())
        date_insert:datetime = self.__cur.fetchone()[0]
        return date_insert

    def get_workday_above_insert_date(self, above_date: datetime.date):
        self.__cur.execute(SQLCommands.get_workday_above_insert_date(above_date))
        return self.__cur.fetchall()

    def get_users_with_group_id(self, group_id: int):
        self.__cur.execute(SQLCommands.get_users_for_update_schedule(group_id))
        return self.__cur.fetchall()

    def commit(self):
        self.__con.commit()