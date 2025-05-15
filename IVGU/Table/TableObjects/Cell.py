from bs4 import BeautifulSoup, ResultSet, Tag


class Cell:
    def get_data_date_from_cell(self,cell: str):
        data = self.__get_raw_data(cell)
        return data.get("data-date")

    @staticmethod
    def __get_raw_data(cell: str) -> Tag:
        data = BeautifulSoup(str(cell), 'html.parser').select(".cell")[0]
        return data

    def get_data_time_from_cell(self,cell: str):
        data = self.__get_raw_data(cell)
        return data.get("data-time")