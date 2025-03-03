from bs4 import BeautifulSoup, Tag, ResultSet

class IVGUConverter:

    def _get_departments_from_page(self, page: str):
        all_tags = self.__get_tags_departments(page)
        all_departments = self.__get_departments_from_tags(all_tags)
        return all_departments

    @staticmethod
    def __get_tags_departments(page:str) ->ResultSet[Tag]:
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

    def _get_institutes_from_page(self,page:str):
        all_tags = self.__get_tags_institutes(page)
        all_institutes = self.__get_institutes_from_tags(all_tags)
        return all_institutes

    @staticmethod
    def __get_tags_institutes(page:str) ->ResultSet[Tag]:
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