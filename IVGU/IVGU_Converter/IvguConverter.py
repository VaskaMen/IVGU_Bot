from bs4 import BeautifulSoup, Tag, ResultSet

import Seecret
from IVGU.Ivgu import Ivgu

class IvguConverter:
    ivgu = Ivgu()

    def __init__(self):
        self.ivgu.login(Seecret.IVGU_LOGIN, Seecret.IVGU_PASSWORD)

    def get_tags_departments(self,institute:int) ->ResultSet[Tag]:
        page = self.ivgu.get_page_of_departments(institute)
        all_tags = BeautifulSoup(page, "html.parser").select('.uk-nav-sub a')
        return all_tags

    def get_departments(self,tags: ResultSet[Tag]) -> dict[str, str]:
        all_departments: dict[str, str] = {}
        for tag in tags:
            key = tag.text
            all_departments[key] = self.get_number_of_department(tag)
        return all_departments

    @staticmethod
    def get_number_of_department(tag:Tag) ->str:
        number = tag.get("href").split('/')[-1]
        return number
