from bs4 import BeautifulSoup, ResultSet, Tag, NavigableString, PageElement
from datetime import datetime, date

from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule
from IVGU.ScheduleObject.Lesson import Lesson
from IVGU.ScheduleObject.WorkDay import WorkDay
from IVGU.Table.TableObjects.Cell import Cell
from IVGU.Table.TableObjects.Constructors import Constructors
from IVGU.Table.TableObjects.Line import Line

class TableConvertor:
    cell = Cell()
    line = Line()
    constr = Constructors()
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
    def get_tbody_of_times(table: str) -> BeautifulSoup:
        tbody = BeautifulSoup(table, "html.parser")
        tbody.find('thead').extract()
        return tbody

    def get_time_table(self,page:str) ->list[str]:
        subject_tables = BeautifulSoup(page, 'html.parser').select('.first-table')
        return self.result_set_to_list_str(subject_tables)

    @staticmethod
    def  get_time_codes(tbody:BeautifulSoup):
        all_times = BeautifulSoup(str(tbody), "html.parser").select('.text-bold.cell.text-center')
        time_codes = {}
        for i in all_times:
            time_codes[f"{i.get('data-time')}"] = i.text
        return time_codes

    @staticmethod
    def result_set_to_list_str(result_set:  ResultSet[PageElement | Tag | NavigableString]) -> list[str]:
        mas = []
        for result in result_set:
            mas.append(str(result))
        return mas

    def get_subject_tables(self,page:str) ->list[str]:
        subject_tables = BeautifulSoup(page, 'html.parser').select('.second-table')
        return self.result_set_to_list_str(subject_tables)

    @staticmethod
    def get_names_of_all_directions(table: str) -> list[str]:
        tr = BeautifulSoup(table, 'html.parser').select('thead tr')[1].select('th')
        directions = []
        for elem in tr:
            elem = str(elem).replace('<',">").split(">")
            directions.append(elem[-3])
        return directions

    @staticmethod
    def have_subgroups(table: str):
        tr = BeautifulSoup(table, 'html.parser').select('thead tr')
        return len(tr) == 4

    def get_direction_schedule(self, table:str, time_table:str) ->list[DirectionSchedule]:
        lessons = self.get_lessons_from_table(table,time_table)
        direction_schedule: list[DirectionSchedule] = []
        for direction in lessons:
            dir_sched = DirectionSchedule(direction,lessons[direction])
            direction_schedule.append(dir_sched)
        return direction_schedule

    def get_lessons_from_table(self,table:str,time_table:str):
        lines = self.line.get_lines_of_subjects(table)
        all_cells = self.line.lines_separator_into_cells(lines)
        have_subgroup = self.have_subgroups(table)
        all_groups = self.get_groups_names(table)
        sorted = self.__sorting_station_for_cells(all_cells, all_groups, have_subgroup)
        tbody = self.get_tbody_of_times(time_table)
        timecodes = self.get_time_codes(tbody)
        all_lessons_to_direction = self.__separate_lessons_to_directions(sorted, timecodes, have_subgroup)
        return all_lessons_to_direction

    def __separate_lessons_to_directions(self, sorted:dict[str, dict[str, list[Tag]]], timecodes:dict[str, str], have_subgroup:bool) ->dict[str, dict[str, WorkDay]]:
        separated: dict[str, dict[str, WorkDay]] = {}
        for direction in sorted:
            separated.setdefault(direction,{})
            lessons_by_dates = self.__lessons_separated_by_dates(sorted[direction],timecodes,have_subgroup)
            separated[direction] = lessons_by_dates

        return separated

    def __lessons_separated_by_dates(self,direction: dict[str, list[Tag]],timecodes:dict[str, str],have_subgroup:bool) -> dict[str, WorkDay]:
        sorted_by_dates:dict[str,WorkDay] = {}
        for day in direction:
            direction.setdefault(day,[])
            list_of_lessons = self.__tags_to_lessons(direction[day], timecodes, have_subgroup)
            converted_date = self.converted_day(day)
            workday = WorkDay(list_of_lessons,converted_date)
            sorted_by_dates[day] = workday
        return sorted_by_dates

    @staticmethod
    def converted_day(raw_date:str) -> date:
        converted_date = datetime.strptime(raw_date,'%Y-%m-%d').date()
        return converted_date

    def __tags_to_lessons(self, lessons_tags: list[Tag], timecodes:dict[str, str], have_subgroup:bool) -> list[Lesson]:
        lessons = []
        group = 1
        for cell in lessons_tags:
            if group == 3:
                group = 1
            lesson = self.__get_lesson(cell, str(group), timecodes, have_subgroup)
            lessons.append(lesson)
            group += 1
        return lessons

    def __sorting_station_for_cells(self, all_cells:ResultSet[Tag], all_groups: list[str], have_subgroup: bool) -> dict[str, dict[str, list[Tag]]]:
        sorted_cells_by_groups = self.cell.cells_sorted_by_groups(all_cells,all_groups,have_subgroup)
        sorted_by_all: dict[str,dict[str,list[Tag]]] = {}
        for sorted in sorted_cells_by_groups:
            sorted_by_all[sorted] = self.cell.cells_sorted_by_dates(sorted_cells_by_groups[sorted])
        return sorted_by_all

    def __get_lesson(self, cell:Tag, group: str, timecodes: dict[str, str], have_group:bool) ->Lesson:
        if cell.text != "" and have_group:
            return self.constr.construct_of_lesson(cell,group,timecodes)
        elif cell.text != "" and  not have_group:
            return self.constr.construct_of_lesson(cell,str(0),timecodes)
        elif have_group:
            return self.constr.construct_of_empty_lesson(cell,group,timecodes)
        else:
            return self.constr.construct_of_empty_lesson(cell,str(0),timecodes)