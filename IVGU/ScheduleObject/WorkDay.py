from datetime import date
from dataclasses import dataclass


from IVGU.ScheduleObject.Lesson import Lesson


@dataclass
class WorkDay:
    lessons: list[Lesson]
    date: date
    subgroup: str