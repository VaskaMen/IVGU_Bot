from datetime import date, datetime


from dataclasses import dataclass


from IVGU.ScheduleObject.Lesson import Lesson

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


@dataclass
class WorkDay:
    lessons: list[Lesson]
    date: date

    def dict(self):
        return {
            'date': date.strftime(self.date,'%Y-%m-%d'),
            'lessons': self.get_dict_lesson()
        }

    def get_dict_lesson(self):
        lessons = []
        for lesson in self.lessons:
            if lesson.subject.name != "":
                lessons.append(lesson.dict())
        return lessons

    def __str__(self) -> str:
        res = f"***{self.date} {week[self.date.weekday()]}***\n\n"
        for i in self.lessons:
            res += f"⌚  ***{i.subject.time}*** \n📘  {i.subject.name} \n🔹  ___{i.subject.type}___ \n"
            for t in i.teacher_places:
                res += f"👨‍🏫  {t.teacher} \n🚪  ***{t.place}***\n"
            res += "\n\n"
        return res
