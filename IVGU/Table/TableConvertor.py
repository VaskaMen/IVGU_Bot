from bs4 import BeautifulSoup, ResultSet, Tag, NavigableString, PageElement

from IVGU.Table.TableObjects.Cell import Cell
from IVGU.Table.TableObjects.Line import Line


class TableConvertor:
    cell = Cell()
    line = Line()
    def get_groups_names(self, table: str) -> list[str]:
        names = []
        table_head = self.__get_table_head(table)
        for elem in table_head:
            elem = str(elem).replace("<",'>')
            names.append(elem.split('>')[-3])
        return names

    @staticmethod
    def __get_table_head(table: str) -> ResultSet[Tag]:
        tr = BeautifulSoup(table, 'html.parser').select('thead tr')
        th = BeautifulSoup(str(tr[1]), 'html.parser').select('th')
        return th

    @staticmethod
    def get_quantity_of_subgroups(table: str):
        tr = BeautifulSoup(table, 'html.parser').select('thead tr')
        return len(tr[-1])

    @staticmethod
    def result_set_to_list_str(result_set:  ResultSet[PageElement | Tag | NavigableString]) -> list[str]:
        mas = []
        for result in result_set:
            mas.append(str(result))
        return mas

    def get_subject_tables(self,page:str) ->list[str]:
        subject_tables = BeautifulSoup(page, 'html.parser').select('.second-table')
        return self.result_set_to_list_str(subject_tables)
