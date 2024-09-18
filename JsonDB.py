import json
from datetime import datetime

from Lesson import Lesson
from Subject import Subject
from TeacherPlace import TeacherPlace
from WorkDay import WorkDay


class JsonDB:

    def add_new_work_days(self, work_days: list[WorkDay]):
        data = self.read_work_days()
        with open('workDays.json', "w", encoding="utf-8") as f:
            for i in work_days:
                data[f"{i.date}"] = i.dict()
            json.dump(data, f, ensure_ascii=False, indent=4)

    def read_work_days(self) -> dict:
        try:
            data: dict
            with open('workDays.json', "r", encoding="utf-8") as json_file:
                data = json.loads(json_file.read())
            return data
        except Exception as ex:
            return {}


    def get_work_days(self) -> list[WorkDay]:
        data = self.read_work_days()
        work_days: list[WorkDay]  = list()
        for i in data:
            print(data[f"{i}"])
            work_days.append( WorkDay(
                date=datetime.strptime(i,'%Y-%m-%d').date(),
                lessons=self.get_lessons_from_dict(data[f"{i}"]['lessons'])
            ))
        return work_days

    def get_lessons_from_dict(self, lessons_dict: dict) -> list[Lesson]:
        lessons: list[Lesson] = list()
        for lesson in lessons_dict:
            lessons.append(
                Lesson(
                    subject=self.get_subject_from_json(lesson['subject']),
                    teacher_place=self.get_teacher_place(lesson['teacher_place'])
                )
            )
        return lessons

    def get_subject_from_json(self, json: dict):
        return Subject(
            time=json['time'],
            name=json['name'],
            type=json['type']
        )

    def get_teacher_place(self, json: list[dict]) -> list[TeacherPlace]:
        teacher_place: list[TeacherPlace] = list()

        for t in json:
            teacher_place.append( TeacherPlace(
                teacher=t['teacher'],
                place=t['place']
            ))
        return teacher_place