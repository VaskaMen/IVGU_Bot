

from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace



class Lesson:
    def __init__(self,subject:Subject=Subject(),teacher_place:list[TeacherPlace]=list(), is_empty:bool=False):
        self.subject = subject
        self.teacher_place = teacher_place

    def dict(self):
        return {
            'subject': self.subject.__dict__,
            'teacher_place': [
                t.__dict__ for t in self.teacher_place
            ]
        }
    def __str__(self):
        return self.dict()