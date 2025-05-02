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
        if "$teacher" in line:
            st = line.split("$teacher")
            st.pop(0)
            st.pop(-1)
            return self.__clean_teachers(st)
        else:
            return ["None,None"]

    @staticmethod
    def get_teacher(teacher_place: str):
        if "(" not in teacher_place:
            return teacher_place.split(",")[0]
        else:
            return ""

    @staticmethod
    def get_place(teacher_place: str) -> str:
        teach_place = teacher_place.split(",")
        if len(teach_place) >= 2:
            correct_teach_place = teach_place[1].strip()
            return correct_teach_place
        else:
            return ""
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

    def lines_sorted_by_dates(self, all_lines: list[str]) ->dict[str, list[str]] :
        sorted_lines: dict[str, list[str]] = {}
        for line in all_lines:
            data = self._get_date_date_from_line(str(line))
            sorted_lines.setdefault(f"{data}",[])
            sorted_lines[f"{data}"].append(line)
        return sorted_lines