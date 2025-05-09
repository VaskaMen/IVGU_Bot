from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB


class ScheduleCollector(SQLDBB):
    api = APIIVGU("miha2204n@gmail.com", "8azr25pb")

    def get_schedules_for_uni_number(self,uni_number: int):
        institutes = self.api.get_institutes(uni_number)
        for institute in institutes:
            self.add_institute(int(institutes[institute]), institute)
            self.get_schedules_for_institute(int(institutes[institute]))

    def get_schedules_for_institute(self, institute: int):
        all_departments = self.api.get_departments(institute)
        for department in all_departments:
            self.add_department(int(all_departments[department]),department,institute)
            self.__get_schedules_for_department(all_departments, department)

    def __get_schedules_for_department(self, all_departments: dict[str, str], department: str):
        all_links = self.api.get_schedule_links_for_department(int(all_departments[department]))
        for link in all_links:
            self.__get_schedules_for_link(link, all_departments, department)

    def __get_schedules_for_link(self, link: str, all_departments: dict[str, str], department: str):
        course = self.api.get_course_from_link(link)
        level = self.api.get_level_from_link(link)
        page = self.api.get_page(link)
        schedules = self.api.get_schedules_from_page(page)
        for schedule in schedules:
            self.add_direction_schedule(schedule, int(all_departments[department]), course, level)