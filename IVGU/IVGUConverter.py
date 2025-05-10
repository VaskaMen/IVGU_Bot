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
            key = tag.text.replace("\n", "")
            all_departments[key] = self.__get_number_of_department(tag)
        return all_departments

    @staticmethod
    def __get_number_of_department(tag: Tag) -> str:
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

    def _get_schedule_links_from_page(self,page:str) -> list[str]:
        all_tags = self.__get_tags_of_schedule(page)
        all_links = self.__get_links_from_tags_of_schedule(all_tags)
        return all_links


    def __get_links_from_tags_of_schedule(self, tags: list[Tag]) ->list[str] :
        all_links = []
        for tag in tags:
            href = self.__get_href_from_tag(tag)
            all_links.append(href)
        return all_links

    @staticmethod
    def __get_tags_of_schedule(page:str) ->list[Tag]:
        all_tags = BeautifulSoup(page, "html.parser").select('a[href^="/info/showschedule/"]')
        filtered_tags = [tag for tag in all_tags if "/exam" not in tag['href']]
        return filtered_tags

    @staticmethod
    def __get_href_from_tag(tag: Tag) -> str:
        href = tag.get("href")
        return href