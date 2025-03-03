class CreateCommands:
    @staticmethod
    def create_table_subjects() -> str:
        return """create table if not exists Subjects
        (
        id integer primary key autoincrement,
        name text
        )
        """
    @staticmethod
    def create_table_teachers() -> str:
        return """create table if not exists Teachers
        (
        id integer primary key autoincrement,
        name text
        )
        """

    @staticmethod
    def create_table_places() -> str:
        return """create table if not exists Places
        (
        id integer primary key autoincrement,
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
    def create_table_levels() -> str:
        return """create table if not exists Levels
        (
        id integer primary key autoincrement,
        name text
        )
        """

    @staticmethod
    def create_table_subgroups() -> str:
        return """create table if not exists Subgroups
        (
        id integer primary key autoincrement,
        name text
        )
        """

    @staticmethod
    def create_table_directions() -> str:
        return """create table if not exists Directions
        (
        id integer primary key autoincrement,
        name text,
        department int
        )
        """

    @staticmethod
    def create_table_groups() -> str:
        return """create table if not exists Groups
        (
        id integer primary key autoincrement,
        course integer,
        subgroup integer,
        level integer,
        direction integer
        )
        """

    @staticmethod
    def create_table_lessons() -> str:
        return """create table if not exists Lessons
        (
        id integer primary key autoincrement,
        subject integer,
        place integer,
        time text,
        type text,
        [date] date,
        [group] integer
        ) 
        """

    @staticmethod
    def create_table_teachers_lesson() -> str:
        return """create table if not exists TeachersLesson
        (
        id integer primary key autoincrement,
        teacher integer,
        lesson integer
        ) 
        """