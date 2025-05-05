from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule

from IVGU.ScheduleObject.WorkDay import WorkDay
from SQLDB.SQLEngine import SQLEngine


class SQLDBB(SQLEngine):

    def add_direction_schedule(self,direction: DirectionSchedule, department_id: int, course: int, level:int):
        direction_id = self.add_direction(direction.direction,department_id)
        id_subdirection = self.add_subdirection(direction.subdirection,direction_id)
        for day in direction.schedule:
            self.add_workday(day,course,level,id_subdirection)

    def add_workday(self, workday: WorkDay,course: int, level: int,id_subdirection: int):
        subgroup = self.add_subgroup(workday.subgroup)
        self.add_group(course,subgroup,level,id_subdirection)
        for lesson in workday.lessons:
            if str(lesson.name) != 'None':
                lesson_id = self.add_lesson(lesson, workday.date, subgroup)
                self._add_many_teacher_place(lesson_id, lesson.teacher_places)