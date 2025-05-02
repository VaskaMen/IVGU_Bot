import sqlite3

from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from SQLDB.SQLCommands.CreateCommands import CreateCommands
from SQLDB.SQLCommands.SQLCommands import SQLCommands
from datetime import date

class SQLEngine:
    def __init__(self):
        self.__con = sqlite3.connect("lesson.db")
        self.__cur = self.__con.cursor()
        self.__cur.execute(CreateCommands.create_table_levels())
        self.__cur.execute(CreateCommands.create_table_institutes())
        self.__cur.execute(CreateCommands.create_table_departments())
        self.__cur.execute(CreateCommands.create_table_groups())
        self.__cur.execute(CreateCommands.create_table_places())
        self.__cur.execute(CreateCommands.create_table_lessons())
        self.__cur.execute(CreateCommands.create_table_directions())
        self.__cur.execute(CreateCommands.create_table_subdirections())
        self.__cur.execute(CreateCommands.create_table_subgroups())
        self.__cur.execute(CreateCommands.create_table_subjects())
        self.__cur.execute(CreateCommands.create_table_teachers())
        self.__cur.execute(CreateCommands.create_table_teachers_lesson())
        self.__con.commit()
        self.__cur.execute(SQLCommands.add_level(1,"Бакалавриат"))
        self.__cur.execute(SQLCommands.add_level(2,"Магистратура"))
        self.__cur.execute(SQLCommands.add_level(3,"Специалитет"))
        self.__con.commit()

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

    def add_subdirection(self, subdirection: str, direction_id: int):
        self.__cur.execute((SQLCommands.add_subdirection(subdirection, direction_id)))

    def add_department(self, id_of_department: int, name: str, id_of_institute: int):
        self.__cur.execute(SQLCommands.add_department(id_of_department, name, id_of_institute))

    def add_institute(self, id_of_institute: int, name: str):
        self.__cur.execute(SQLCommands.add_institute(id_of_institute, name))

    def add_lesson(self, lesson: Lesson, date_: date, subgroup: int):
        subject = self._add_subject(lesson)
        self.__cur.execute(SQLCommands.add_lesson(subject, lesson.time, lesson.type_subject, str(date_), subgroup))
        self.__cur.execute(SQLCommands.find_id_lesson(subject, lesson.time, lesson.type_subject, str(date_), subgroup))
        return self.__cur.fetchone()[0]


    def commit(self):
        self.__con.commit()