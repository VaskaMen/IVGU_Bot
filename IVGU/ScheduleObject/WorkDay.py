from datetime import date
from dataclasses import dataclass


from IVGU.ScheduleObject.Lesson import Lesson

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

@dataclass
class WorkDay:
    lessons: list[Lesson]
    date: date
    subgroup: str

    def __eq__(self, other):
        if isinstance(other,WorkDay):
            return self.date == other.date and self.subgroup == other.subgroup and self.lessons == other.lessons
        return False

    def __str__(self) -> str:
        if len(self.lessons) != 0:
            res = f"***{self.date} {week[self.date.weekday()]}***\n\n"
            for lesson in self.lessons:
                res += f"⌚  ***{lesson.time}*** \n📘  {lesson.name} \n🔹  ___{lesson.type_subject}___ \n"
                for teacher_place in lesson.teacher_places:
                    res += f"👨‍🏫  {teacher_place.teacher} \n🚪  ***{teacher_place.place}***\n"
                res += "\n\n"
            return res
        else:
            return """Нет расписания на этот день."""