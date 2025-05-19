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
    def find_place_id(place: str) -> str:
        return f"""select id from Places where place = '{place}'"""

    @staticmethod
    def add_department(id_of_dep: int, name: str, institute_id: int) -> str:
        return  f"""INSERT INTO Departments (id, name, institute)
                SELECT {id_of_dep},'{name}',{institute_id}
                WHERE NOT EXISTS (
                SELECT 1 FROM Departments WHERE id = {id_of_dep}
                )"""



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
        return f"""INSERT INTO Users (id,"group",teacher_id, update)
                    SELECT {id_user}, {group_id}, {teacher_id}, {False}"""

    @staticmethod
    def update_user(id_user: int, group_id: int, teacher_id: int = 0) -> str:
        return f"""Update Users set "group" = {group_id}, teacher_id = {teacher_id}  where id = {id_user}"""

    @staticmethod
    def update_schedule_user(update: bool, id_user: int,):
        return f"""Update Users set update = {update} where id = {id_user}"""

    @staticmethod
    def user_select(id_user: int) -> str:
        return f"""Select "group" from Users where users.id = {id_user}"""

    @staticmethod
    def get_teachers_of_lesson(lesson_id: int) -> str:
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
    def get_dates_after_date(group_id: int, date: str) -> str:
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
    def get_teacher_dates_after_date(teacher_id: int, date: str) -> str:
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
        workday.id in (select max(workday.id) from workday group by "date", workday.group) AND
        workday.date >= '{date}'
        
        group by workday.date
        order by workday.date"""

    @staticmethod
    def find_teacher_id_by_name(teacher_name: str) -> str:
        return f"""select Teachers.id
        from Teachers
        where Teachers.name like '%{teacher_name}%'"""

    @staticmethod
    def find_teachers_group() -> str:
        return f"""select Groups.id
        from Groups
        where Groups.course = -1"""

    @staticmethod
    def find_user_teacher_id(user_id: int) -> str:
        return f"""select teacher_id
        from Users 
        where Users.id = {user_id}"""

    @staticmethod
    def update_if_teach_to_student(user_id: int) -> str:
        return f'''Update Users set "teacher_id" = 0 where id = {user_id}'''

    @staticmethod
    def get_teachers_workday(date: str, teacher_id: int) -> str:
        return f"""select
        lessons.time_start as "Время начала",
        lessons.time_end as "Время конца",
        max(subjects.name) as "Предмет",
        max(types.name) as "Тип",
        max(lessons.id) as "id lesson"
        
        from Lessons
        
        left join Teachersplace
        on lessons.id = Teachersplace.lesson
        
        left join workday
        on Lessons.workday = workday.id
        
        left join subjects
        on Lessons.subject = subjects.id
        
        left join Types
        on lessons.type = Types.id
        
        where teachersplace.teacher = {teacher_id} and 
        workday.id in (select max(workday.id) from workday group by "date", workday.group) and
        workday.date = '{date}'
        group by lessons.time_start, lessons.time_end, workday.date
        order by workday.date, lessons.time_start"""

    @staticmethod
    def add_workday(date: datetime.date, group_id: int) -> str:
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
    def find_last_workday(date: datetime.date, group_id: int) -> str:
        return f"""select *
        from Workday 
        where "date" = '{date}' and "group" = {group_id}
		order by workday.insert_date desc limit 1"""

    @staticmethod
    def find_workday_lessons(workday_id: int) -> str:
        return f'''select
                    max(lessons.time_start) as "Время начала",
                    max(lessons.time_end) as "Время конца",
                    max(subjects.name) as "Предмет",
                    max(types.name),
                    max(lessons.id)
                    
                    from Lessons
                    
                    left join Teachersplace
                    on lessons.id = Teachersplace.lesson
                    
                    
                    left join workday
                    on Lessons.workday = workday.id
                    
                    left join subjects
                    on Lessons.subject = subjects.id
                    
                    left join Types
                    on lessons.type = Types.id
                    
                    where workday.id = {workday_id}
                    group by lessons.time_start
		'''

    @staticmethod
    def get_date_subgroup_by_workday(workday_id: int) -> str:
        return f"""select workday.date,
		subgroups.name
		from workday

		left join Groups
		on workday.group = Groups.id

		left join Subgroups
		on groups.subgroup = Subgroups.id
		
		where workday.id = {workday_id}"""

    @staticmethod
    def get_last_insert_date_workday() -> str:
        return f"""
            SELECT insert_date 
            FROM public.workday 
            ORDER BY insert_date desc 
            limit 1
                """

    @staticmethod
    def get_workday_above_insert_date(above_date: datetime.date) -> str:
        return f"""
                SELECT max(workday.id), max(workday.date), max(workday.insert_date), max(workday.group)
                FROM public.workday 
                where insert_date > '{above_date}'
                group by workday.date
                """

    @staticmethod
    def get_users_for_update_schedule(group_id: int) -> str:
        return  f"""
                SELECT * 
                FROM users
                where users.group = {group_id} AND
                users.update = {True}
                """

