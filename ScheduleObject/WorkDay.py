from datetime import date

from attr import dataclass

from ScheduleObject.Lesson import Lesson


@dataclass
class WorkDay:
    lessons: list[Lesson]
    date: date

    def dict(self):
        return {
            'date': f"{self.date.year}-{self.date.month}-{self.date.day}",
            'lessons': [
                l.dict() for l in self.lessons
            ]
        }


