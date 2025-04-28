from datetime import date


from dataclasses import dataclass


from IVGU.ScheduleObject.Lesson import Lesson

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


@dataclass
class WorkDay:
    lessons: list[Lesson]
    date: date
    subgroup: str

    def __str__(self) -> str:
        res = f"***{self.date} {week[self.date.weekday()]}***\n\n"
        for i in self.lessons:
            res += f"⌚  ***{self.subgroup}*** \n📘 \n"
            res += f"⌚  ***{i.time}*** \n📘  {i.name} \n🔹  ___{i.type_subject}___ \n"
            for t in i.teacher_places:
                res += f"👨‍🏫  {t.teacher} \n🚪  ***{t.place}***\n"
            res += "\n\n"
        return res
