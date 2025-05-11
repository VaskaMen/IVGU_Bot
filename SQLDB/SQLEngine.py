import sqlite3
from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace
from SQLDB.SQLCommands.CreateCommands import CreateCommands
from SQLDB.SQLCommands.SQLCommands import SQLCommands
from datetime import date

class SQLEngine:
    def __init__(self):
        self.__con = sqlite3.connect("Schedules.db", check_same_thread=False, isolation_level=None)
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
        self.__con.commit()
        self.__cur.execute(SQLCommands.add_level(1,"Бакалавриат"))
        self.__cur.execute(SQLCommands.add_level(2,"Магистратура"))
        self.__cur.execute(SQLCommands.add_level(3,"Специалитет"))
        self.__cur.execute(SQLCommands.add_level(4,"ДОП"))
        self.__cur.execute(SQLCommands.add_form(6,'Очная Форма обучения'))
        self.__cur.execute(SQLCommands.add_form(8,'Очно-заочная Форма обучения'))
        self.__cur.execute(SQLCommands.add_form(7,'Заочная Форма обучения'))
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

    def add_lesson(self, lesson: Lesson, date_: date, subgroup: int):
        subject = self._add_subject(lesson)
        type_for_lesson = self.add_type(lesson.type_subject)
        self.__cur.execute(SQLCommands.add_lesson(subject, lesson.time, type_for_lesson, str(date_), subgroup))
        self.__cur.execute(SQLCommands.find_id_lesson(subject, lesson.time, type_for_lesson, str(date_), subgroup))
        return self.__cur.fetchone()[0]

    def add_group(self, course: int, subgroup: int, level: int,form: int, subdirection: int):
        self.__cur.execute(SQLCommands.add_group(course, subgroup, level, form, subdirection))
        self.__cur.execute(SQLCommands.find_id_group(course, subgroup, level, form, subdirection))
        return self.__cur.fetchone()[0]

    def add_type(self, name: str) -> int:
        self.__cur.execute(SQLCommands.add_type(name))
        self.__cur.execute(SQLCommands.find_type_id_by_name(name))
        return self.__cur.fetchone()[0]

    def _get_list_institutes(self) -> list[tuple[str]]:
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

    def add_user(self,user_id: int,group_id: int):
        return self.__cur.execute(SQLCommands.add_user(user_id, group_id))

    def commit(self):
        self.__con.commit()