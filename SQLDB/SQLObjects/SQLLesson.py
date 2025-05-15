import datetime
from SQLDB.SQLObjects.SQLTeacherPlace import SQLTeacherPlace


class SQLLesson:
    def __init__(self, subject_name: str,
                 time_start: datetime.time,
                 time_end: datetime.time,
                 type_name: str,
                 date: datetime.date,
                 teach_places: list[SQLTeacherPlace]):
        self.subject_name = subject_name
        self.time_start = time_start
        self.time_end = time_end
        self.type_name = type_name
        self.date = date
        self.teach_places = teach_places
