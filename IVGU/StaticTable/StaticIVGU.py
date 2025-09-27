from datetime import datetime

from IVGU.StaticTable.Convertor import Convertor
from IVGU.StaticTable.StaticIVGUPage import StaticIVGUPage


class StaticIVGU:
    __ivgu = StaticIVGUPage()
    __convertor = Convertor()

    def download_all_schedules(self):
        schedules = self.get_all_schedule_download_links()
        self.download_schedules(schedules)

    def get_all_schedule_download_links(self) -> list[str]:
        institutes = self.get_all_institute_schedule_link()
        schedule_download_links = []
        for institute in institutes:
            schedule_download_links.extend(self.get_schedule_download_link(institute))
        return schedule_download_links

    def get_all_institute_schedule_link(self) -> list[str]:
        page = self.__ivgu.get_schedule_institute_page()
        return  self.__convertor.get_institute_schedule_link(page)


    def get_schedule_download_link(self, institute_schedule_link: str) -> list[str]:
        institute_schedule = self.__ivgu.get_page(institute_schedule_link).text
        return self.__convertor.get_schedule_link(institute_schedule)


    def download_schedules(self, download_links: list[str]):
        for i, link in enumerate(download_links):
            pdf = self.__ivgu.get_page(link).content
            with open(f"schedule/schedule_{i}.pdf", "wb") as file:
                file.write(pdf)
