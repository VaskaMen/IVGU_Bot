class LineConvertor:
    @staticmethod
    def __get_date_time_code_from_line(line:str) -> str:
        return line.split("$")[1].split("~")[1]

    @staticmethod
    def _get_date_date_from_line(line:str) -> str:
        return line.split("$")[2].split("~")[1]

    @staticmethod
    def __get_raw_lesson_from_line(line:str) -> str:
        if "lesson" in line:
            return line.split("$")[3].split("lesson")[1].strip()
        else:
            return "None (None)"

    def _get_type_of_subject(self, line: str) -> str:
        lesson = self.__get_raw_lesson_from_line(line)
        return lesson.replace(")","(").split("(")[1]

    def _get_name_of_lesson(self, line: str) -> str:
        lesson = self.__get_raw_lesson_from_line(line)
        return lesson.split("(")[0].rstrip()

    def get_teachers_with_place(self, line: str) -> list[str]:
        st = line.split("$teacher")
        st.pop(0)
        st.pop(-1)
        return self.__clean_teachers(st)

    @staticmethod
    def get_teacher(teacher_place: str):
       return teacher_place.split(",")[0]

    @staticmethod
    def get_place(teacher_place: str) -> str:
       return teacher_place.split(",")[1].strip()

    @staticmethod
    def __clean_teachers(line: list[str]) -> list[str]:
        new_line = []
        for elem in line:
            el = elem.strip()
            if el != '':
                new_line.append(el)
        return new_line

    def _get_time(self, line, timecodes) -> str:
        raw_time = self.__get_date_time_code_from_line(line)
        time = timecodes[raw_time]
        return time
