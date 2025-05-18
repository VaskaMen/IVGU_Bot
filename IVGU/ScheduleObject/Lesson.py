from typing import Any

from IVGU.ScheduleObject.TeacherPlace import TeacherPlace



class Lesson:
    def __init__(self, time: str = "", name: str = "", type_subject: str = "", teacher_place: list[TeacherPlace] = list()):
        self.teacher_places = teacher_place
        self.time = time
        self.name = name
        self.type_subject = type_subject

    def dict(self):
        return {
            'subject': self.name,
            'time': self.time,
            'type_subject': self.type_subject,
            'teacher_place': [
                teacher_place.__dict__ for teacher_place in self.teacher_places
            ]
        }

    def __eq__(self, other):
        if isinstance(other, Lesson):
            if self.time == other.time and self.name == other.name and self.type_subject == other.type_subject:
              return self.soft_compare(self.teacher_places, other.teacher_places)
        return False

    @staticmethod
    def soft_compare(list_1: list[Any], list_2: list[Any]):
        flag = True
        for i in list_1:
            flag = i in list_2
            if not flag:
                break
        return flag

    def __str__(self):
        return str(self.dict())