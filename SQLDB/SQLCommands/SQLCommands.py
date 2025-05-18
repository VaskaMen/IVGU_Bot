from datetime import datetime


class SQLCommands:

    @staticmethod
    def add_subject(name: str) -> str:
        return  f"""INSERT INTO Subjects (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Subjects WHERE name = '{name}'
                )"""
    @staticmethod
    def find_subject_id_by_name(name: str) -> str:
        return f"""SELECT id FROM Subjects WHERE name = '{name}'
        """

    @staticmethod
    def find_subject_by_name(name: str) -> str:
        return f"""select * from Subjects where name = '{name}'"""

    @staticmethod
    def find_subject_by_id(id: int) -> str:
        return f"""select * from Subjects where id = {id}"""

    @staticmethod
    def add_teacher(name: str) -> str:
        return  f"""INSERT INTO Teachers (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Teachers WHERE name = '{name}'
                )"""

    @staticmethod
    def find_id_teacher(name: str) -> str:
        return f"""SELECT id FROM Teachers WHERE name = '{name}'"""

    @staticmethod
    def find_teacher_by_name(name: str) -> str:
        return f"""select * from Teachers where name = '{name}'"""

    @staticmethod
    def find_teacher_by_id(id: int) -> str:
        return f"""select * from Teachers where id = {id}"""

    @staticmethod
    def add_teachers_of_lesson(teacher_id: int, lesson_id: int, place_id: int) -> str:
        return  f"""INSERT INTO TeachersPlace (teacher, lesson, place)
                SELECT {teacher_id},{lesson_id},{place_id}
                WHERE NOT EXISTS (
                SELECT 1 FROM TeachersPlace WHERE teacher = {teacher_id} AND lesson = {lesson_id} AND place ={place_id}
                )"""

    @staticmethod
    def find_id_teachers_of_lesson_by_ids(teacher_id: int, lesson_id: int, place_id: int) -> str:
        return f"""SELECT id FROM TeachersPlace WHERE 
                    teacher = {teacher_id} AND
                    lesson = {lesson_id} AND
                    place ={place_id}
                    )"""

    @staticmethod
    def find_teacher_of_lesson_by_lesson_id(lesson_id: int) -> str:
        return f"""select * from TeachersPlace where lesson = {lesson_id}"""

    @staticmethod
    def add_place(place: str) -> str:
        return  f"""INSERT INTO Places (place)
                SELECT '{place}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Places WHERE place = '{place}'
                )"""

    @staticmethod
    def find_place_by_place(place: str) -> str:
        return f"""select * from Places where place = '{place}'"""

    @staticmethod
    def find_place_id(place: str) -> str:
        return f"""select id from Places where place = '{place}'"""

    @staticmethod
    def find_place_by_id(id: int) -> str:
        return f"""select * from Places where id = {id}"""

    @staticmethod
    def add_department(id_of_dep: int, name: str, institute_id: int) -> str:
        return  f"""INSERT INTO Departments (id, name, institute)
                SELECT {id_of_dep},'{name}',{institute_id}
                WHERE NOT EXISTS (
                SELECT 1 FROM Departments WHERE id = {id_of_dep}
                )"""

    @staticmethod
    def find_department_by_number(number: str) -> str:
        return f"""select * from Departments where number = '{number}'"""

    @staticmethod
    def find_department_by_id(id: int) -> str:
        return f"""select * from Departments where id = {id}"""

    @staticmethod
    def add_institute(id_institute: int,name: str) -> str:
        return  f"""INSERT INTO Institutes (id,name)
                SELECT {id_institute},'{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Institutes WHERE id = {id_institute}
                )"""

    @staticmethod
    def add_direction(name:str, id_department: int) -> str:
        return  f"""INSERT INTO Directions (name,department)
                SELECT '{name}',{id_department}
                WHERE NOT EXISTS (
                SELECT 1 FROM Directions WHERE name = '{name}' and department = {id_department}
                )"""

    @staticmethod
    def find_direction_id(name: str, id_department: int) -> str:
        return  f"""SELECT id FROM Directions WHERE 
                name = '{name}' AND
                department = {id_department}"""

    @staticmethod
    def add_subdirection(name: str, id_direction: int) -> str:
        return  f"""INSERT INTO SubDirections (name,direction)
                SELECT '{name}',{id_direction}
                WHERE NOT EXISTS (
                SELECT 1 FROM SubDirections WHERE name = '{name}'
                )"""

    @staticmethod
    def find_subdirection_id(name: str, id_direction: int) -> str:
        return f"""SELECT id FROM SubDirections WHERE 
            name = '{name}' AND
            direction = {id_direction}"""

    @staticmethod
    def add_level(id: int, name: str) -> str:
        return  f"""INSERT INTO Levels (id,name)
                SELECT {id},'{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Levels WHERE id = {id}
                )"""

    @staticmethod
    def add_form(id: int, name: str) ->str:
        return f"""INSERT INTO Forms (id,name)
                SELECT {id},'{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Forms WHERE id = {id}
                )"""

    @staticmethod
    def add_subgroup(name: str) -> str:
        return  f"""INSERT INTO Subgroups (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Subgroups WHERE name = '{name}'
                )"""
    @staticmethod
    def find_id_subgroup(name: str) -> str:
        return f"""SELECT id FROM Subgroups WHERE name = '{name}'"""

    @staticmethod
    def add_group(course: int, subgroup_id: int, level_id: int,form_id: int, subdirection_id: int) -> str:
        return  f"""INSERT INTO Groups (course,subgroup,level,form,subdirection)
                SELECT {course},{subgroup_id},{level_id},{form_id},{subdirection_id}
                WHERE NOT EXISTS (
                SELECT 1 FROM Groups WHERE
                 course = {course} AND
                 subgroup = {subgroup_id} AND
                 level = {level_id} AND
                 form = {form_id} AND
                 subdirection = {subdirection_id}
                )"""

    @staticmethod
    def add_type(name: str) -> str:
        return f"""INSERT INTO Types (name)
                SELECT '{name}'
                WHERE NOT EXISTS (
                SELECT 1 FROM Types WHERE name = '{name}'
                )"""

    @staticmethod
    def find_type_id_by_name(name: str) -> str:
        return f"""select * from Types where name = '{name}'"""

    @staticmethod
    def add_lesson(subject_id: int, time_start: str,time_end: str, type: int, workday: int) -> str:
        return f"""insert into Lessons(
            subject,
            time_start,
            time_end,
            type,
            workday
        )
         SELECT
            {subject_id},
            '{time_start}',
            '{time_end}',
            '{type}',
            {workday}
            
         WHERE NOT EXISTS (
            SELECT 1 FROM Lessons WHERE 
            subject = {subject_id} AND
            time_start = '{time_start}' AND
            time_end = '{time_end}' AND
            type = '{type}' AND
            workday = {workday}
            )
            """

    @staticmethod
    def find_id_lesson(subject_id: int, time_start: str, time_end:str, type: int, workday: int) -> str:
        return f"""SELECT id FROM Lessons WHERE 
            subject = {subject_id} AND
            time_start = '{time_start}' AND
            time_end = '{time_end}' AND
            type = {type}  AND
            workday = {workday} 
            """

    @staticmethod
    def find_id_group(course_id: int, subgroup_id: int, level_id: int,form_id: int, subdirection_id: int) -> str:
        return f"""SELECT id FROM Groups WHERE 
            course = {course_id} AND
            subgroup = {subgroup_id} AND
            level = {level_id} AND
            form = {form_id} AND
            subdirection = {subdirection_id}"""

    @staticmethod
    def select_all_institutes():
        return f"""SELECT Institutes.name from Institutes"""

    @staticmethod
    def select_all_institute_departments(institute: str):
        return f"""SELECT 
        Departments.name
        
        from Departments

        LEFT JOIN Institutes
        on Departments.institute = Institutes.id

        where Institutes.name like '{institute}'"""

    @staticmethod
    def select_all_department_forms(department: str):
        return f"""SELECT 
        Forms.name
        
        from Groups
    
        LEFT JOIN SubDirections
        on Groups.subdirection = SubDirections.id
    
        LEFT JOIN Directions
        on SubDirections.direction = Directions.id
    
        LEFT JOIN Forms
        on Groups.form = Forms.id
    
        LEFT JOIN Departments
        on Directions.department = Departments.id
    
        where departments.name like '{department}'
    
        group by Forms.name"""

    @staticmethod
    def select_all_department_form_levels(department: str, form: str):
        return f"""SELECT 
        Levels.name

        from Groups
        
        LEFT JOIN Levels
        on Groups.level = Levels.id
        
        LEFT JOIN SubDirections
        on Groups.subdirection = SubDirections.id
        
        LEFT JOIN Directions
        on SubDirections.direction = Directions.id
        
        LEFT JOIN Forms
        on Groups.form = Forms.id
        
        LEFT JOIN Departments
        on Directions.department = Departments.id
        
        where departments.name like '{department}' AND
        Forms.name like '{form}'
        
        group by Levels.name"""

    @staticmethod
    def select_all_courses(department: str, form: str, level: str):
        return f"""SELECT 
        Groups.course

        from Groups
        
        LEFT JOIN Levels
        on Groups.level = Levels.id
        
        LEFT JOIN SubDirections
        on Groups.subdirection = SubDirections.id
        
        LEFT JOIN Directions
        on SubDirections.direction = Directions.id
        
        LEFT JOIN Forms
        on Groups.form = Forms.id
        
        LEFT JOIN Departments
        on Directions.department = Departments.id
        
        WHERE Departments.name like '{department}' AND
        Forms.name like '{form}' AND
        Levels.name like '{level}'
        
        group by Groups.course"""

    @staticmethod
    def get_directions(department: str, form: str, level: str, course: str | int):
        return f"""SELECT 
        Directions.name

        from Groups
        
        
        LEFT JOIN Levels
        on Groups.level = Levels.id
        
        LEFT JOIN SubDirections
        on Groups.subdirection = SubDirections.id
        
        LEFT JOIN Directions
        on SubDirections.direction = Directions.id
        
        LEFT JOIN Forms
        on Groups.form = Forms.id
        
        LEFT JOIN Departments
        on Directions.department = Departments.id
        
        WHERE departments.name like '{department}' AND
        Forms.name like '{form}' AND
        Levels.name like '{level}' AND
        Groups.course = {course}
        
        group by Directions.name"""

    @staticmethod
    def get_subdirections(department: str, form: str, level: str, course: str | int, direction: str):
        return f"""SELECT 
            Subdirections.name

            from Groups


            LEFT JOIN Levels
            on Groups.level = Levels.id

            LEFT JOIN SubDirections
            on Groups.subdirection = SubDirections.id

            LEFT JOIN Directions
            on SubDirections.direction = Directions.id

            LEFT JOIN Forms
            on Groups.form = Forms.id

            LEFT JOIN Departments
            on Directions.department = Departments.id

            WHERE departments.name like '{department}' AND
            Forms.name like '{form}' AND
            Levels.name like '{level}' AND
            Groups.course = {course} AND
            Directions.name like '%{direction}%'

            group by Subdirections.name"""

    @staticmethod
    def get_subgroups(department: str, form: str, level: str, course: str | int,direction: str, subdirection: str):
        return f"""SELECT 
        Subgroups.name as "Подгруппа"

        from Groups
        
        LEFT JOIN Subgroups
        on Groups.subgroup = Subgroups.id
        
        LEFT JOIN Levels
        on Groups.level = Levels.id
        
        LEFT JOIN SubDirections
        on Groups.subdirection = SubDirections.id
        
        LEFT JOIN Directions
        on SubDirections.direction = Directions.id
        
        LEFT JOIN Forms
        on Groups.form = Forms.id
        
        LEFT JOIN Departments
        on Directions.department = Departments.id
        
        WHERE departments.name like '{department}' AND
        Forms.name like '{form}' AND
        Levels.name like '{level}' AND
        Groups.course = {course} AND
        Directions.name like '%{direction}%' AND
        Subdirections.name like '%{subdirection}%'
        
        group by Subgroups.name"""

    @staticmethod
    def get_group_id(department: str, form: str, level: str, course: str | int,direction: str, subdirection: str, subgroup: str):
        return f"""SELECT 
        Groups.id

        from Groups
        
        LEFT JOIN Subgroups
        on Groups.subgroup = Subgroups.id
        
        LEFT JOIN Levels
        on Groups.level = Levels.id
        
        LEFT JOIN SubDirections
        on Groups.subdirection = SubDirections.id
        
        LEFT JOIN Directions
        on SubDirections.direction = Directions.id
        
        LEFT JOIN Forms
        on Groups.form = Forms.id
        
        LEFT JOIN Departments
        on Directions.department = Departments.id
        
        WHERE departments.name like '{department}' AND
        Forms.name like '{form}' AND
        Levels.name like '{level}' AND
        Groups.course = {course} AND
        Directions.name like '%{direction}%' AND
        Subdirections.name like '%{subdirection}%' AND
        Subgroups.name like '{subgroup}'
        
        group by Groups.id"""

    @staticmethod
    def insert_user(id_user: int, group_id: int, teacher_id: int = 0) -> str:
        return f"""INSERT INTO Users (id,"group",teacher_id)
                    SELECT {id_user}, {group_id}, {teacher_id}"""

    @staticmethod
    def update_user(id_user: int, group_id: int, teacher_id: int = 0) -> str:
        return f"""Update Users set "group" = {group_id}, teacher_id = {teacher_id}  where id = {id_user}"""

    @staticmethod
    def user_select(id_user: int):
        return f"""Select "group" from Users where users.id = {id_user}"""

    @staticmethod
    def get_workday(group_id: int, date: str):
        return f"""select 

                    Subjects.name as "Предмет",
                    Lessons.time_start,
                    Lessons.time_end,
                    Types.name as "Тип",
                    Workday."date",
                    Lessons.id
                    
                    from Lessons
                    
                    Left join Workday
                    ON Lessons.workday = Workday.id
                    
                    Left join Subjects
                    ON Lessons.subject = Subjects.id
                    
                    left join Types
                    ON Lessons.type = Types.id	
                    
                    where 
                    Workday.group = {group_id} AND
                    Workday.date = '{date}'
                    
                    order by time_start
        """

    @staticmethod
    def get_teachers_of_lesson(lesson_id: int):
        return f"""select
        Teachers.name,
        Places.place
        
        from TeachersPlace
        
        left join Places
        on TeachersPlace.place = Places.id
        
        left join Teachers
        on TeachersPlace.teacher = Teachers.id
        
        left join Lessons
        on TeachersPlace.lesson = Lessons.id
        
        where Lessons.id = {lesson_id}"""

    @staticmethod
    def get_dates_after_date(group_id: int, date: str):
        return f'''select   
                    Workday."date"
                    
                    from Lessons
                    
                    left join Workday
                    on Lessons.workday = Workday.id
                    
                    where 
                    Workday.group = {group_id} AND
                    Workday.date >= '{date}'

					group by workday."date"
                    order by workday."date"'''

    @staticmethod
    def get_teacher_dates_after_date(teacher_id: int, date: str):
        return f"""select	
		
        workday.date
    
        from TeachersPlace

		left join lessons
		on TeachersPlace.lesson = Lessons.id

		LEFT join workday
		on Lessons.workday = workday.id

		left join teachers
		on TeachersPlace.teacher = Teachers.id

		
        
        where teachers.id = {teacher_id} AND
        workday.date >= '{date}'
        
        group by workday.date
        order by workday.date"""

    @staticmethod
    def find_teacher_id_by_name(teacher_name: str):
        return f"""select Teachers.id
        from Teachers
        where Teachers.name like '%{teacher_name}%'"""

    @staticmethod
    def find_teachers_group():
        return f"""select Groups.id
        from Groups
        where Groups.course = -1"""

    @staticmethod
    def find_user_teacher_id(user_id: int):
        return f"""select teacher_id
        from Users 
        where Users.id = {user_id}"""

    @staticmethod
    def update_if_teach_to_student(user_id: int):
        return f'''Update Users set "teacher_id" = 0 where id = {user_id}'''

    @staticmethod
    def get_teachers_workday(date: str, teachers_id: int):
        return f"""select 
        max(Subjects.name) as "Предмет",
        max(Lessons.time_start) as "Начало",
        max(Lessons.time_end) as "Конец",
        max(Types.name) as "Тип",
        max(workday.date) as "Дата",
        max(Lessons.id) as "id"
        
        from TeachersPlace
        
        left join Lessons
        on TeachersPlace.lesson = Lessons.id

		left join workday
		on lessons.workday = workday.id
        
        left join Teachers
        on TeachersPlace.teacher = Teachers.id
        
        Left Join Subjects
        on Lessons.subject = Subjects.id
        
        Left Join Types
        on Lessons.type = Types.id
        
        where workday.date = '{date}' and Teachers.id = {teachers_id}
        group by Lessons.time_start
        order by Lessons.time_start"""

    @staticmethod
    def add_workday(date: datetime.date, group_id: int):
        return  f"""
            insert into Workday(
              "date",
              insert_date,
              "group"
            )
            values( 
                '{date}',
                NOW(),
                {group_id}
                )
                """


    @staticmethod
    def find_workday(date: datetime.date, group_id: int):
        return f"""select *
        from Workday 
        where "date" = '{date}' and "group" = {group_id} """

    @staticmethod
    def find_teacher_place(teacher_id: int, place_id: int) -> str:
        return f"""
             SELECT
                id
             from TeachersPlace
             WHERE
                teacher = {teacher_id} AND
                place = {place_id}
                    
                """