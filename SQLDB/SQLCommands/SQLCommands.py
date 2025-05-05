class SQLCommands:

    @staticmethod
    def add_subject(name:str):
        return  f"""INSERT INTO Subjects (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Subjects WHERE name = '{name}'
                )"""
    @staticmethod
    def find_subject_id_by_name(name: str):
        return f"""SELECT id FROM Subjects WHERE name = '{name}'
        """

    @staticmethod
    def find_subject_by_name(name:str):
        return f"""select * from Subjects where name = '{name}'"""

    @staticmethod
    def find_subject_by_id(id:int):
        return f"""select * from Subjects where id = {id}"""

    @staticmethod
    def add_teacher(name:str):
        return  f"""INSERT INTO Teachers (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Teachers WHERE name = '{name}'
                )"""

    @staticmethod
    def find_id_teacher( name: str):
        return f"""SELECT id FROM Teachers WHERE name = '{name}'"""

    @staticmethod
    def find_teacher_by_name(name:str):
        return f"""select * from Teachers where name = '{name}'"""

    @staticmethod
    def find_teacher_by_id(id:int):
        return f"""select * from Teachers where id = {id}"""

    @staticmethod
    def add_teachers_of_lesson(teacher_id: int,lesson_id:int, place_id: int):
        return  f"""INSERT INTO TeachersLesson (teacher,lesson,place)
                SELECT {teacher_id},{lesson_id},{place_id}
                WHERE NOT EXISTS (
                SELECT 1 FROM TeachersLesson WHERE teacher = {teacher_id} AND lesson = {lesson_id} AND place ={place_id}
                )"""

    @staticmethod
    def find_id_teachers_of_lesson_by_ids(teacher_id: int, lesson_id: int, place_id: int):
        return f"""SELECT id FROM TeachersLesson WHERE 
                    teacher = {teacher_id} AND
                    lesson = {lesson_id} AND
                    place ={place_id}
                    )"""

    @staticmethod
    def find_teacher_of_lesson_by_lesson_id(lesson_id:int):
        return f"""select * from TeachersLesson where lesson = {lesson_id}"""

    @staticmethod
    def add_place(place:str):
        return  f"""INSERT INTO Places (place)
                SELECT '{place}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Places WHERE place = '{place}'
                )"""

    @staticmethod
    def find_place_by_place(place:str):
        return f"""select * from Places where place = '{place}'"""

    @staticmethod
    def find_place_id(place: str):
        return f"""select id from Places where place = '{place}'"""

    @staticmethod
    def find_place_by_id(id:int):
        return f"""select * from Places where id = {id}"""

    @staticmethod
    def add_department(id_of_dep:int,name: str,institute_id: int):
        return  f"""INSERT INTO Departments (id, name, institute)
                SELECT {id_of_dep},'{name}',{institute_id}
                WHERE NOT EXISTS (
                SELECT 1 FROM Departments WHERE id = {id_of_dep}
                )"""

    @staticmethod
    def find_department_by_number(number:str):
        return f"""select * from Departments where number = '{number}'"""

    @staticmethod
    def find_department_by_id(id:int):
        return f"""select * from Departments where id = {id}"""

    @staticmethod
    def add_institute(id_institute: int,name: str):
        return  f"""INSERT INTO Institutes (id,name)
                SELECT {id_institute},'{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Institutes WHERE id = {id_institute}
                )"""

    @staticmethod
    def add_direction(name:str, id_department: int):
        return  f"""INSERT INTO Directions (name,department)
                SELECT '{name}',{id_department}
                WHERE NOT EXISTS (
                SELECT 1 FROM Directions WHERE name = '{name}'
                )"""

    @staticmethod
    def find_direction_id(name: str, id_department: int):
        return  f"""SELECT id FROM Directions WHERE 
                name = '{name}' AND
                department = {id_department}"""

    @staticmethod
    def add_subdirection(name: str, id_direction: int):
        return  f"""INSERT INTO SubDirections (name,direction)
                SELECT '{name}',{id_direction}
                WHERE NOT EXISTS (
                SELECT 1 FROM SubDirections WHERE name = '{name}'
                )"""

    @staticmethod
    def find_subdirection_id(name: str, id_direction: int):
        return f"""SELECT id FROM SubDirections WHERE 
            name = '{name}' AND
            direction = {id_direction}"""

    @staticmethod
    def add_level(id:int,name:str):
        return  f"""INSERT INTO Levels (id,name)
                SELECT {id},'{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Levels WHERE id = {id}
                )"""

    @staticmethod
    def add_subgroup(name:str):
        return  f"""INSERT INTO Subgroups (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Subgroups WHERE name = '{name}'
                )"""
    @staticmethod
    def find_id_subgroup(name: str):
        return f"""SELECT id FROM Subgroups WHERE name = '{name}'"""

    @staticmethod
    def add_group(course:int, subgroup_id:int, level_id:int, subdirection_id:int):
        return  f"""INSERT INTO Groups (course,subgroup,level,subdirection)
                SELECT {course},{subgroup_id},{level_id},{subdirection_id}
                WHERE NOT EXISTS (
                SELECT 1 FROM Groups WHERE
                 course = {course} AND
                 subgroup = {subgroup_id} AND
                 level = {level_id} AND
                 subdirection = {subdirection_id}
                )"""

    @staticmethod
    def add_type(name: str):
        return f"""INSERT INTO Types (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Types WHERE name = '{name}'
                )"""

    @staticmethod
    def find_type_id_by_name(name: str) -> str:
        return f"""select * from Types where name = '{name}'"""

    @staticmethod
    def add_lesson(subject_id: int, time: str, type: int, date: str, group_id: int) -> str:
        return f"""insert into Lessons(
            subject,
            time,
            type,
            date,
            [group]
        )
         SELECT
            {subject_id},
            '{time}',
            '{type}',
            '{date}',
            {group_id}  
         WHERE NOT EXISTS (
            SELECT 1 FROM Lessons WHERE 
            subject = {subject_id} AND
            time = '{time}' AND
            type = '{type}' AND
            [date] = {date} AND
            [group] = {group_id}
                )
            """
    @staticmethod
    def find_id_lesson(subject_id: int, time: str, type: int, date: str, group_id: int) -> str:
        return f"""SELECT id FROM Lessons WHERE 
            subject = {subject_id} AND
            time = '{time}' AND
            type = {type} AND
            [date] = '{date}' AND
            [group] = {group_id}"""

    @staticmethod
    def find_id_group(course_id: int, subgroup_id: int, level_id: int, subdirection_id: int):
        return f"""SELECT id FROM Groups WHERE 
            course = {course_id} AND
            subgroup = {subgroup_id} AND
            level = {level_id} AND
            subdirection = {subdirection_id}"""