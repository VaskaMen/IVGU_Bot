class LineConvertor:
    @staticmethod
    def __get_date_time_code_from_line(line:str) -> str:
        return line.split("$")[1].split("~")[1]

    @staticmethod
    def get_date_date_from_line(line:str) -> str:
        return line.split("$")[2].split("~")[1]

    @staticmethod
    def __get_raw_lesson_from_line(line:str) -> str:
        return line.split("$")[3].split("lesson")[1].strip()

    def get_type_of_subject(self, line: str):
        lesson = self.__get_raw_lesson_from_line(line)
        return lesson.replace(")","(").split("(")[1]

    def get_name_of_lesson(self,line:str):
        lesson = self.__get_raw_lesson_from_line(line)
        return lesson.split("(")[0].rstrip()

    def get_teachers_from_line(self,line: str) -> list[str]:
        st = line.split("$teacher")
        st.pop(0)
        st.pop(-1)
        return self.__clean_teachers(st)

    @staticmethod
    def __clean_teachers(line: list[str]) ->list[str]:
        new_line = []
        for elem in line:
            el = elem.strip()
            if el != '':
                new_line.append(el)
        return new_line

    def get_time(self,line,timecodes):
        raw_time = self.__get_date_time_code_from_line(line)
        time = timecodes[raw_time]
        return time

st1 = "$date_time~13~  $date_date~2025-04-26~  $lesson  Английский язык в сфере профессиональной коммуникации (практическое занятие)  (Факультатив)  $lesson  $teacher  Доцент Мелентьева О.А., Д - Дистанционно  $teacher  $teacher  Доцент Москалева С.И., Д - Дистанционно  $teacher  $date_date~2025-04-26~  $date_time~13~"




lncon = LineConvertor()
print(lncon.get_date_date_from_line(st1))
print(lncon.__get_date_time_code_from_line(st1))
print(lncon.get_teachers_from_line(st1))
print(lncon.get_type_of_subject(st1))
print(lncon.get_name_of_lesson(st1))