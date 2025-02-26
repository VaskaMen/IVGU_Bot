

from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace



class Lesson:
    def __init__(self,subject:Subject=Subject(),teacher_place:list[TeacherPlace]=list(), is_empty:bool=False):
        self.subject = subject
        self.teacher_places = teacher_place

    def dict(self):
        return {
            'subject': self.subject.__dict__,
            'teacher_place': [
                teacher_place.__dict__ for teacher_place in self.teacher_places
            ]
        }
    def __str__(self):
        return self.dict()