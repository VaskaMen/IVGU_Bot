from dataclasses import dataclass

from IVGU.ScheduleObject.WorkDay import WorkDay

@dataclass
class DirectionSchedule:
    direction: str
    schedule: list[WorkDay]

    def __eq__(self, other):
        if other is DirectionSchedule:
            if self.direction == other.direction:
                return True
        return False