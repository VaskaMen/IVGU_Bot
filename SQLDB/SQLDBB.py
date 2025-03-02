import sqlite3

from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from SQLDB.SQLCommands.CreateCommands import CreateCommands
from SQLDB.SQLCommands.SQLCommands import SQLCommands


class SQLDBB:
    def __init__(self):
        self.con = sqlite3.connect("lesson.db")
        self.cur = self.con.cursor()
        self.cur.execute(CreateCommands.create_table_levels())
        self.cur.execute(CreateCommands.create_table_departments())
        self.cur.execute(CreateCommands.create_table_groups())
        self.cur.execute(CreateCommands.create_table_places())
        self.cur.execute(CreateCommands.create_table_lessons())
        self.cur.execute(CreateCommands.create_table_directions())
        self.cur.execute(CreateCommands.create_table_subgroups())
        self.cur.execute(CreateCommands.create_table_subjects())
        self.cur.execute(CreateCommands.create_table_teachers())
        self.cur.execute(CreateCommands.create_table_teachers_lesson())
        self.con.commit()

    def add_subject(self, subject: Subject):
        self.cur.execute(SQLCommands.add_subject(subject.name))
        self.con.commit()

    def add_teacher_place(self,teachplace: TeacherPlace):
        self.cur.execute(SQLCommands.add_teacher(teachplace.teacher))
        self.cur.execute(SQLCommands.add_place(teachplace.place))
        self.con.commit()

    def add_lesson(self,lesson: Lesson):
        self.add_subject(lesson.subject)
        for teacher_place in lesson.teacher_places:
            self.add_teacher_place(teacher_place)
        self.con.commit()