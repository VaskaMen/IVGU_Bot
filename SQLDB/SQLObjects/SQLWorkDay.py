from datetime import date

from SQLDB.SQLObjects.SQLLesson import SQLLesson

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

class SQLWorkDay:
    def __init__(self, lessons: list[SQLLesson], date: date):
        self.lessons = lessons
        self.date = date

    def __str__(self) -> str:
        if len(self.lessons) != 0:
            res = f"***{self.date} {week[self.date.weekday()]}***\n\n"
            for lesson in self.lessons:
                time = lesson.time_start + " - " + lesson.time_end
                res += f"⌚  ***{time}*** \n📘  {lesson.subject_name} \n🔹  ___{lesson.type_name}___ \n"
                for teacher_place in lesson.teach_places:
                    res += f"👨‍🏫  {teacher_place.teacher} \n🚪  ***{teacher_place.place}***\n"
                res += "\n\n"
            return res
        else:
            return """Нет расписания на этот день."""