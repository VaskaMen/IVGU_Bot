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
    def __str__(self):
        return str(self.dict())