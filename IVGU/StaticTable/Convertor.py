from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag
from bs4.element import AttributeValueList


class Convertor:

    def get_institute_schedule_link(self, institute_page: str) -> list[str]:
        tags = BeautifulSoup(institute_page, "html.parser").select('body > div.container.container-main.col-margin > div > div.col.col-mb-12.col-8.col-dt-9 > div.white-box.col-margin-bottom.padding-box a')
        links = []
        for tag in tags:
            links.append(self.__get_href(tag))
        return links

    def __get_href(self, tag: Tag):
        return tag.get("href")

    def get_schedule_link(self, schedule_page: str) -> list[str]:
        tags = BeautifulSoup(schedule_page, "html.parser").select('body > div.container.container-main.col-margin > div > div.col.col-mb-12.col-8.col-dt-9 > div.white-box.col-margin-bottom.padding-box > div > div:nth-child(4) a[href^="/upload/medialibrary"]')
        links = []
        for tag in tags:
            links.append(self.__get_href(tag))
        return links