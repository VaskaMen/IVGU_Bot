import sqlite3

from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule
from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from SQLDB.SQLCommands.CreateCommands import CreateCommands
from SQLDB.SQLCommands.SQLCommands import SQLCommands


class SQLDBB:
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
        self.__cur.execute(CreateCommands.create_table_subgroups())
        self.__cur.execute(CreateCommands.create_table_subjects())
        self.__cur.execute(CreateCommands.create_table_teachers())
        self.__cur.execute(CreateCommands.create_table_teachers_lesson())
        self.__con.commit()
        self.__cur.execute(SQLCommands.add_level(1,"Бакалавриат"))
        self.__cur.execute(SQLCommands.add_level(2,"Магистратура"))
        self.__cur.execute(SQLCommands.add_level(3,"Специалитет"))
        self.__con.commit()

    def add_subject(self, subject: Subject):
        self.__cur.execute(SQLCommands.add_subject(subject.name))

    def add_teacher_place(self,teachplace: TeacherPlace):
        self.__cur.execute(SQLCommands.add_teacher(teachplace.teacher))
        self.__cur.execute(SQLCommands.add_place(teachplace.place))

    def add_direction_schedule(self,direction: DirectionSchedule,department_id:int):
        self.add_direction(direction.direction,department_id)
        for day in direction.schedule:
            for lesson in direction.schedule[day].lessons:
                    self.add_lesson(lesson)

    def add_lesson(self,lesson: Lesson):
        self.add_subject(lesson.subject)
        for teacher_place in lesson.teacher_places:
            self.add_teacher_place(teacher_place)

    def add_subgroup(self, subgroup_name: str):
        self.__cur.execute(SQLCommands.add_subgroup(subgroup_name))

    def add_direction(self,direction: str, department_id: int):
        self.__cur.execute(SQLCommands.add_direction(direction, department_id))

    def add_department(self, id_of_department: int, name:str, id_of_institute: int):
        self.__cur.execute(SQLCommands.add_department(id_of_department, name,id_of_institute))

    def add_institute(self,id_of_institute: int,name: str):
        self.__cur.execute(SQLCommands.add_institute(id_of_institute,name))

    def commit(self):
        self.__con.commit()
