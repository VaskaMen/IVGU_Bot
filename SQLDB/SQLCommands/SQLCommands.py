class SQLCommands:

    @staticmethod
    def add_subject(name:str):
        return f"""insert or ignore into Subject(name) values('{name}')"""

    @staticmethod
    def find_subject_by_name(name:str):
        return f"""select * from Subject where name = '{name}'"""

    @staticmethod
    def find_subject_by_id(id:int):
        return f"""select * from Subject where id = {id}"""

    @staticmethod
    def add_teacher(name:str):
        return f"""INSERT INTO Teachers (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Teachers WHERE name = '{name}'
                )"""

    @staticmethod
    def find_teacher_by_name(name:str):
        return f"""select * from Teachers where name = '{name}'"""

    @staticmethod
    def find_teacher_by_id(id:int):
        return f"""select * from Teachers where id = {id}"""

    @staticmethod
    def add_teachers_of_lesson(teacher_id: int,lesson_id:int):
        return f"""insert or ignore into TeachersLesson(teacher, lesson) values({teacher_id},{lesson_id})"""

    @staticmethod
    def find_teacher_of_lesson_by_lesson_id(lesson_id:int):
        return f"""select * from TeachersLesson where lesson = {lesson_id}"""

    @staticmethod
    def add_place(place:str):
        return f"""insert or ignore into Places(place) values('{place}')"""

    @staticmethod
    def find_place_by_place(place:str):
        return f"""select * from Places where place = '{place}'"""

    @staticmethod
    def find_place_by_id(id:int):
        return f"""select * from Places where id = {id}"""

    @staticmethod
    def add_department(number:str):
        return f"""insert or ignore into Departments(number) values('{number}')"""

    @staticmethod
    def find_department_by_number(number:str):
        return f"""select * from Departments where number = '{number}'"""

    @staticmethod
    def find_department_by_id(id:int):
        return f"""select * from Departments where id = {id}"""

    @staticmethod
    def add_direction(name:str, id_department: int):
        return f"""insert or ignore into Directions(name,department) values('{name}',{id_department})"""

    @staticmethod
    def add_level(name:str):
        return f"""insert or ignore into Levels(name) values('{name}')"""

    @staticmethod
    def add_subgroup(name:str):
        return f"""insert or ignore into Subgroups(name) values('{name}')"""

    @staticmethod
    def add_group(course:int,subgroup_id:int,level_id:int,direction_id:int):
        return f"""insert or ignore into Levels(course,subgroup,level,direction)
         values({course},{subgroup_id}),{level_id},{direction_id}"""

    @staticmethod
    def add_lesson(subject_id:int,place_id:int,time:str,type:str,date:str,group_id: int):
        return f"""insert or ignore into Levels(subject,place,time,type,date,group)
         values({subject_id},{place_id}),'{time}','{type}','{date}',{group_id}"""
