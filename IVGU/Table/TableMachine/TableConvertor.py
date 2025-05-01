from bs4 import BeautifulSoup, ResultSet, Tag
from pandas import Index

from IVGU.Table.TableMachine.Constructors import Constructors




class TableConvertor(Constructors):
    def split_directions(self,table:str) -> BeautifulSoup:
        directions = self.__get_table_head_directions(table)
        splitted_directions = self.tags_splitter(directions)

        bs = BeautifulSoup(table, 'html.parser')
        tr = bs.select('thead tr')
        tr[2].clear()
        self.insert_tags(tr[2], splitted_directions)
        return bs

    @staticmethod
    def __get_table_head_directions(table: str) -> ResultSet[Tag]:
        tr = BeautifulSoup(table, 'html.parser').select('thead tr')
        th = BeautifulSoup(str(tr[2]), 'html.parser').select('th')
        return th

    @staticmethod
    def tags_splitter(td: ResultSet[Tag]) -> ResultSet[Tag]:
        for id,elem in enumerate(td):
            colspan = elem.get("colspan")
            if colspan is not None:
                elem["colspan"] = "1"
                for i in range(int(colspan)-1):
                    td.insert(id+i, elem)
        return td

    @staticmethod
    def insert_tags(tag_to_insert: Tag, tags: ResultSet[Tag]):
        for tag in tags:
            copy = tag.copy_self()
            copy.append(tag.text)
            tag_to_insert.append(copy)


    @staticmethod
    def get_all_directions(keys: Index) -> list[str]:
        all_directions = []
        for key in keys:
            if "Направление" in key[0]:
                all_directions.append(key[0])
        return all_directions


