from dataclasses import dataclass

from IVGU.ScheduleObject.WorkDay import WorkDay

@dataclass
class DirectionSchedule:
    direction: str
    schedule: dict[str,WorkDay]

    def dict(self):
        return {
            'direction': self.direction ,
            'schedule': self.get_dict_workday()
        }

    def get_dict_workday(self):
        schedule = {}
        for keys in self.schedule:
            schedule[f'{keys}'] = self.schedule[f"{keys}"].dict()
        return schedule