from bs4 import BeautifulSoup, Tag, ResultSet

import Seecret
from IVGU.Ivgu import Ivgu

class IvguConverter:
    ivgu = Ivgu()

    def __init__(self):
        self.ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

    def get_departments(self,institute: int) -> dict[str, str]:
        all_tags = self.__get_tags_departments(institute)
        all_departments = self.__get_departments_from_tags(all_tags)
        return all_departments

    def __get_tags_departments(self, institute:int) ->ResultSet[Tag]:
        page = self.ivgu.get_page_of_departments(institute)
        all_tags = BeautifulSoup(page, "html.parser").select('.uk-nav-sub a[href^="/info/chair/"]')
        return all_tags

    def __get_departments_from_tags(self, tags: ResultSet[Tag]) -> dict[str, str]:
        all_departments: dict[str, str] = {}
        for tag in tags:
            key = tag.text
            all_departments[key] = self.__get_number_of_department(tag)
        return all_departments

    @staticmethod
    def __get_number_of_department(tag:Tag) -> str:
        number = tag.get("href").split('/')[-1]
        return number

    def get_institutes(self,university_number: int) -> dict[str, str]:
        all_tags = self.__get_tags_institutes(university_number)
        all_institutes = self.__get_institutes_from_tags(all_tags)
        return all_institutes

    def __get_tags_institutes(self, university_number: int) ->ResultSet[Tag]:
        page = self.ivgu.get_page_of_institutes(university_number)
        all_tags = BeautifulSoup(page, "html.parser").select('.uk-nav-sub a[href^="/info/institutes/"]')
        return all_tags

    def __get_institutes_from_tags(self, tags: ResultSet[Tag]) -> dict[str, str]:
        all_institutes: dict[str, str] = {}
        for tag in tags:
            key = tag.text
            all_institutes[key] = self.__get_number_of_institute(tag)
        return all_institutes

    @staticmethod
    def __get_number_of_institute(tag: Tag) -> str:
        number = tag.get("href").split('/')[-1]
        return number