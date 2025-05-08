from bs4 import BeautifulSoup, ResultSet, Tag


from IVGU.Table.TableMachine.Constructors import Constructors


class TableConvertor(Constructors):
    table: BeautifulSoup

    def __init__(self, table: str):
        super()
        self.table = BeautifulSoup(table, 'html.parser')

    def set_new_table(self, table: str):
        self.table = BeautifulSoup(table, 'html.parser')

    def split_subdirections(self):
        subdirections = self.__get_table_head_subdirections()
        splitted_subdirections = self.__tags_splitter_by_colspan(subdirections)
        splitted_subdirections = self.__tags_splitter_by_rowspan(splitted_subdirections)
        tr = self.table.select('thead tr')
        tr[2].clear()
        self.__insert_tags(tr[2], splitted_subdirections)
        return

    def duplicate_last_tr(self):
        list_tr = self.table.select("thead tr")
        thead = self.table.select("thead")[0]
        if len(list_tr) < 4:
            self.__insert_tag(thead,list_tr[-1])


    @staticmethod
    def __tags_splitter_by_rowspan(tr: ResultSet[Tag]) -> ResultSet[Tag]:
        for id, elem in enumerate(tr):
            rowspan = elem.get("rowspan")
            if rowspan is not None:
                elem["rowspan"] = "0"
                for i in range(int(rowspan) - 1):
                    tr.insert(id + i, elem)
        return tr

    def split_directions(self):
        directions = self.__get_table_head_directions()

        splitted_directions: ResultSet[Tag] = ResultSet(None)
        for direction in directions:
            data_index: int = int(direction.get('data-idx'))
            direction_spilt_count = self.__count_data_index(data_index) - 1
            splitted_directions.extend(self.__tags_splitter(direction, direction_spilt_count))
        tr = self.table.select('thead tr')
        tr[1].clear()
        self.__insert_tags(tr[1], splitted_directions)
        return

    def __count_data_index(self, index: int):
        return len(self.table.select(f'thead th[data-idx="{index}"]'))

    def __get_table_head_directions(self) -> ResultSet[Tag]:
        tr = self.table.select('thead tr')
        th = tr[1].select('th')
        return th

    def __get_table_head_subdirections(self) -> ResultSet[Tag]:
        tr = self.table.select('thead tr')
        th = tr[2].select('th')
        return th

    def __get_table_head_group(self) -> ResultSet[Tag]:
        tr = self.table.select('thead tr')
        th = tr[3].select('th')
        return th

    @staticmethod
    def __tags_splitter_by_colspan(td: ResultSet[Tag]) -> ResultSet[Tag]:
        for id,elem in enumerate(td):
            colspan = elem.get("colspan")
            if colspan is not None:
                elem["colspan"] = "1"
                for i in range(int(colspan)-1):
                    td.insert(id+i, elem)
        return td

    @staticmethod
    def __tags_splitter(td: Tag, times: int, ) -> ResultSet[Tag]:
        new_tds: ResultSet[Tag] = ResultSet(None)
        for i in range(times):
            new_tds.insert(i, td)
        return new_tds

    def __insert_tags(self, tag_to_insert: Tag, tags: ResultSet[Tag]):
        for tag in tags:
            self.__insert_tag(tag_to_insert,tag)

    @staticmethod
    def __insert_tag(tag_to_insert: Tag, tag: Tag):
        copy = tag.copy_self()
        copy.append(tag.text)
        tag_to_insert.append(copy)