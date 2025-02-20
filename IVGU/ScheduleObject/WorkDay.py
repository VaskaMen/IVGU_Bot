from datetime import date


from dataclasses import dataclass


from IVGU.ScheduleObject.Lesson import Lesson

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


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

    def __str__(self) -> str:
        res = f"***{self.date} {week[self.date.weekday()]}***\n\n"
        for i in self.lessons:
            res += f"⌚  ***{i.subject.time}*** \n📘  {i.subject.name} \n🔹  ___{i.subject.type}___ \n"
            for t in i.teacher_place:
                res += f"👨‍🏫  {t.teacher} \n🚪  ***{t.place}***\n"
            res += "\n\n"
        return res
