from datetime import date
from dataclasses import dataclass


from IVGU.ScheduleObject.Lesson import Lesson


@dataclass
class WorkDay:
    lessons: list[Lesson]
    date: date
    subgroup: str

    def __eq__(self, other):
        if isinstance(other,WorkDay):
            return self.date == other.date and self.subgroup == other.subgroup and self.lessons == other.lessons
        return False
