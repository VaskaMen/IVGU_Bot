from io import StringIO
import pandas as pd
from bs4 import ResultSet, Tag

from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule
from IVGU.Table.TableMachine.TableConvertor import TableConvertor
from IVGU.Table.TableMachine.TableExtractor import TableExtractor
from IVGU.Table.TableMachine.TableMarkup import TableMarkup
from IVGU.Table.TableObjects.Cell import Cell


class Table:
    __cel = Cell()
    __tbc: TableConvertor
    __tableex = TableExtractor()

    def get_schedules_from_page(self, page: str) -> list[DirectionSchedule]:
        tables = self.__tableex.get_subject_tables(page)
        time_table = self.__tableex.get_time_table(page)
        timecodes = self.__tableex.get_time_codes(time_table)
        return self.__get_direction_schedules_from_tables(tables, timecodes)

    def __get_direction_schedules_from_tables(self, tables: ResultSet[Tag], timecodes: dict[str,str]):
        all_direction_schedules = []
        for table in tables:
            self.__tbc = TableConvertor(str(table))
            all_direction_schedules.extend(self.__get_direction_schedules_from_table(timecodes))
        return all_direction_schedules

    def __get_direction_schedules_from_table(self, timecodes: dict[str,str]):
        reforged_table = self.__prepare_table()
        panda = pd.read_html(reforged_table)
        direction_schedules = self.__tbc.get_direction_schedules(timecodes, panda[0])
        return direction_schedules

    def __prepare_table(self) -> StringIO:
        self.__tbc.split_subdirections()
        self.__tbc.split_directions()
        self.__tbc.remove_bad_first_tr()
        tbmark = TableMarkup(str(self.__tbc.table))
        tbmark.table_markup()
        srtio = StringIO(tbmark.table.prettify())
        return srtio