from attr import dataclass

from IVGU.ScheduleObject.Subject import Subject
from IVGU.ScheduleObject.TeacherPlace import TeacherPlace


@dataclass
class Lesson:
    subject: Subject
    teacher_place: list[TeacherPlace]

    def dict(self):
        return {
            'subject': self.subject.__dict__,
            'teacher_place': [
                t.__dict__ for t in self.teacher_place
            ]
        }