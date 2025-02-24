from bs4 import BeautifulSoup, ResultSet, Tag, NavigableString, PageElement
from datetime import datetime
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

    def get_lessons_from_table(self,table:str,time_table:str):
        lines = self.line.get_lines_of_subjects(table)
        all_cells = self.line.lines_separator_into_cells(lines)
        have_group = self.have_subgroups(table)
        all_groups = self.get_groups_names(table)
        sorted_cells_by_groups = self.cell.cells_sorted_by_groups(all_cells,all_groups,have_group)
        sorted_by_all: dict[str,dict[str,list[Tag]]] = {}
        for sorted in sorted_cells_by_groups:
            sorted_by_all[sorted] = self.cell.cells_sorted_by_dates(sorted_cells_by_groups[sorted])
        tbody = self.get_tbody_of_times(time_table)
        timecodes = self.get_time_codes(tbody)
        group = 1
        mas: dict[str, dict[str, list[Lesson]]] = {}
        for direction in sorted_by_all:
            mas.setdefault(direction,{})
            for day in sorted_by_all[direction]:
                mas[direction].setdefault(day,[])
                for cell in sorted_by_all[direction][day]:
                    if group == 2:
                        group = 1
                    lessons = self.__get_lesson(cell, str(group), timecodes, have_group)
                    mas[direction][f"{day}"].append(lessons)
                    group += 1
        return mas

    def __get_lesson(self, cell:Tag, group: str, timecodes: dict[str, str], have_group:bool) ->Lesson:
        if cell.text != "" and have_group:
            return self.constr.construct_of_lesson(cell,group,timecodes)
        elif cell.text != "" and  not have_group:
            return self.constr.construct_of_lesson(cell,str(0),timecodes)
        elif have_group:
            return self.constr.construct_of_empty_lesson(cell,group,timecodes)
        else:
            return self.constr.construct_of_empty_lesson(cell,str(0),timecodes)

    def get_workdays_from_table(self,table: str,time_table:str) ->list[WorkDay]:
        lessons = self.get_lessons_from_table(table,time_table)
        list_of_workdays = []
        for date in lessons:
            list = lessons[f"{date}"]
            converted_date = datetime.strptime(date,'%Y-%m-%d')
            list_of_workdays.append(WorkDay(list,converted_date))
        return list_of_workdays

    # def get_group_schedule(self,table: str,time_table:str) -> list[GroupSchedule]:
    #     workdays = self.get_workdays_from_table(table,time_table)
    #
    # def get_sorted_workdays(self,table:str) ->dict[str, list[WorkDay]]:
    #     sorted_workdays: dict[str, list[WorkDay]] = {}
    #     all_directions = self.get_names_of_all_directions(table)
    #     for direction in all_directions:
    #         sorted_workdays.setdefault(f"{direction}",[])
    #         sorted_workdays[f"{direction}"].append()
