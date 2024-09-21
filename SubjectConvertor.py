from bs4 import BeautifulSoup, ResultSet, PageElement

from ScheduleObject.Lesson import Lesson
from ScheduleObject.Subject import Subject
from ScheduleObject.TeacherPlace import TeacherPlace


class SubjectConvertor:

    def get_lessons(self, html: str) -> list[Lesson]:
        lessons: list[Lesson] = list()
        subject = self.get_subjects(html)
        teacher_place = self.get_teacher_place(html)

        for i in range(0, len(subject)):
            lessons.append(
                Lesson(
                    subject=subject[i],
                    teacher_place=teacher_place[i]
                )
            )
        return  lessons


    def get_subjects(self, html: str) -> list[Subject]:
        subjects: list[Subject] = list()
        subject_lines = self.__find_subjects_lines(html)
        for line in subject_lines:
            subjects.append(
                Subject(
                    name=self.__find_subject_name(line),
                    time=self.__find_subject_time(line),
                    type=self.__find_subject_type(line)
                )
            )
        return subjects

    def get_teacher_place(self, html: str) -> list[list[TeacherPlace]]:
        teacher_place_list: list[list[TeacherPlace]] = list(list())
        teacher_place_lines = self.__find_teacher_place_lines(html)
        for line in teacher_place_lines:
            teacher_place_list.append(
                self.__get_inner_place(line)
            )
        return teacher_place_list


    def __get_inner_place(self, line: PageElement) -> list[TeacherPlace]:
        list_inner: list[TeacherPlace] = list()
        inner = line.find_all('li')
        for i in inner:
            list_inner.append(
                TeacherPlace(
                    teacher=self.__find_teacher(i),
                    place=self.__find_place(i)
                )
            )
        return list_inner


    @staticmethod
    def __find_subjects_lines(html: str) -> ResultSet[PageElement]:
        res = BeautifulSoup(html, 'html.parser').find_all('b')
        return res[1:]

    @staticmethod
    def __find_subject_name(element: PageElement) -> str:
        return element.text.split(',')[1].split('(')[0].strip()

    @staticmethod
    def __find_subject_time(element: PageElement) -> str:
        return element.text.split(',')[0]

    @staticmethod
    def __find_subject_type(element: PageElement) -> str:
        return element.text.split(',', maxsplit=1)[1].split('(')[1].replace(")", "")

    @staticmethod
    def __find_teacher_place_lines(html: str) -> ResultSet[PageElement]:
        res = BeautifulSoup(html, 'html.parser')
        return  res.find_all('ul')

    @staticmethod
    def __find_teacher(element: PageElement) -> str:
        return element.text.split(',')[0]

    @staticmethod
    def __find_place(element: PageElement) -> str:
        return element.text.split(',')[1]