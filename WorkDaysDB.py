import json
from datetime import datetime

from JsonDBBase import JsonDBBase
from ScheduleObject.Lesson import Lesson
from ScheduleObject.Subject import Subject
from ScheduleObject.TeacherPlace import TeacherPlace
from ScheduleObject.WorkDay import WorkDay


class WorkDaysDB(JsonDBBase):

    def add_new_work_days(self, work_days: list[WorkDay]):
        data = self.read_file()
        with open('workDays.json', "w", encoding="utf-8") as f:
            for i in work_days:
                data[f"{i.date}"] = i.dict()
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_work_days(self) -> list[WorkDay]:
        data = self.read_file()
        return self.json_to_work_days(data)

    def json_to_work_days(self, json: dict) -> list[WorkDay]:
        work_days: list[WorkDay]  = list()
        for i in json:
            work_days.append( WorkDay(
                date=datetime.strptime(i,'%Y-%m-%d').date(),
                lessons=self.json_to_lessons(json[f"{i}"]['lessons'])
            ))
        return work_days

    def json_to_lessons(self, lessons_dict: dict) -> list[Lesson]:
        lessons: list[Lesson] = list()
        for lesson in lessons_dict:
            lessons.append(
                Lesson(
                    subject=self.json_to_subject(lesson['subject']),
                    teacher_place=self.json_to_teacher_place(lesson['teacher_place'])
                )
            )
        return lessons

    def json_to_subject(self, json: dict):
        return Subject(
            time=json['time'],
            name=json['name'],
            type=json['type']
        )

    def json_to_teacher_place(self, json: list[dict]) -> list[TeacherPlace]:
        teacher_place: list[TeacherPlace] = list()

        for t in json:
            teacher_place.append( TeacherPlace(
                teacher=t['teacher'],
                place=t['place']
            ))
        return teacher_place

    def get_diferens_work_days(self, w1: list[WorkDay], w2:[WorkDay]):
        dif = []
        for w in w1:
            if w not in w2:
                dif.append(w)
        return dif
