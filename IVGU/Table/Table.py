from io import StringIO
import pandas as pd
from bs4 import ResultSet, Tag

from IVGU.Table.TableConvertor import TableConvertor
from IVGU.Table.TableExtractor import TableExtractor
from IVGU.Table.TableMarkup import TableMarkup
from IVGU.Table.TableObjects.Cell import Cell


class Table:
    __cel = Cell()
    __tbc = TableConvertor()
    __tableex = TableExtractor()

    def prepare_table(self,table: Tag) -> StringIO:
        modifided_table = self.__tbc.split_directions(str(table))
        tbmark = TableMarkup(str(modifided_table))
        tbmark.table_markup()
        srtio = StringIO(tbmark.table.prettify())
        return srtio

    def get_schedule(self):
        page = page._get_schedule_page(129,6,1,3,2)
        tables = self.__tableex.get_subject_tables(page)
        time_table = self.__tableex.get_time_table(page)
        timecodes = self.__tableex.get_time_codes(time_table)
        reforged_table = self.prepare_table(tables[0])
        panda = pd.read_html(reforged_table)
        direction_schedules = self.__tbc.get_direction_schedules(timecodes, panda[0])