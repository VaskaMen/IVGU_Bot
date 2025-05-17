class CreateCommands:
    @staticmethod
    def create_table_subjects() -> str:
        return """create table if not exists Subjects
        (
        id serial primary key,
        name text
        )
        """
    @staticmethod
    def create_table_teachers() -> str:
        return """create table if not exists Teachers
        (
        id serial primary key,
        name text
        )
        """

    @staticmethod
    def create_table_places() -> str:
        return """create table if not exists Places
        (
        id serial primary key,
        place text
        )
        """

    @staticmethod
    def create_table_institutes():
        return """create table if not exists Institutes
        (
        id integer primary key,
        name text
        )
        """

    @staticmethod
    def create_table_departments() -> str:
        return """create table if not exists Departments
        (
        id integer primary key,
        name text,
        institute int
        )
        """

    @staticmethod
    def create_table_forms() -> str:
        return """create table if not exists Forms
        (
        id integer primary key,
        name text
        )
        """

    @staticmethod
    def create_table_levels() -> str:
        return """create table if not exists Levels
        (
        id integer primary key,
        name text
        )
        """

    @staticmethod
    def create_table_subgroups() -> str:
        return """create table if not exists Subgroups
        (
        id serial primary key,
        name text
        )
        """

    @staticmethod
    def create_table_directions() -> str:
        return """create table if not exists Directions
        (
        id serial primary key,
        name text,
        department int
        )
        """

    @staticmethod
    def create_table_subdirections() -> str:
        return """create table if not exists SubDirections
        (
        id serial primary key,
        name text,
        direction int
        )
        """

    @staticmethod
    def create_table_groups() -> str:
        return """create table if not exists Groups
        (
        id serial primary key,
        course integer,
        subgroup integer,
        level integer,
        form integer,
        subdirection integer
        )
        """

    @staticmethod
    def create_table_types() -> str:
        return """create table if not exists Types
        (
        id serial primary key,
        name text
        ) 
        """

    @staticmethod
    def create_table_lessons() -> str:
        return """create table if not exists Lessons
        (
        id serial primary key,
        subject integer,
        time_start time,
        time_end time,
        type int,
        teachers_place integer 
        ) 
        """

    @staticmethod
    def create_table_teachers_lesson() -> str:
        return """create table if not exists TeachersPlace
        (
        id serial primary key,
        teacher integer,
        place integer,
        lesson integer
        ) 
        """

    @staticmethod
    def create_table_users() -> str:
        return """create table if not exists Users
        (
        id BIGINT primary key,
        "group" integer,
        teacher_id integer
        )
        """

    @staticmethod
    def create_table_lessons_workday() -> str:
        return """create table if not exists WorkdayLessons
           (
           id serial primary key,
           lessons integer,
           workday integer
           )
           """

    @staticmethod
    def create_table_workday() -> str:
        return """create table if not exists Workday
             (
             id serial primary key,
             "date" date,
             insert_date timestamp,
             "group" integer
             )
             """