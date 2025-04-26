# from IVGU.IVGUPage import IVGUPage
# from IVGU.IVGUConverter import IVGUConverter
# from IVGU.ScheduleObject.DirectionSchedule import DirectionSchedule
# from IVGU.Table.TableConvertor import TableConvertor
#
#
# class APIIVGU(IVGUPage, IVGUConverter):
#     __tablecon = TableConvertor()
#
#     def get_departments(self,institute: int) -> dict[str, str]:
#         page = self._get_page_of_departments(institute)
#         all_departments = self._get_departments_from_page(page)
#         return all_departments
#
#     def get_institutes(self,university_number: int) -> dict[str, str]:
#         page = self._get_page_of_institutes(university_number)
#         all_institutes = self._get_institutes_from_page(page)
#         return all_institutes
#
#     def get_schedules(self, department: int, training_form: int, level:int, course:int, term: int) -> list[DirectionSchedule] :
#         page = self._get_schedule_page(department, training_form, level, course, term)
#         tables = self.__tablecon.get_subject_tables(page)
#         time_tables = self.__tablecon.get_time_table(page)
#
#         all_schedules = []
#         schedule_for_first_week = self.__tablecon.get_direction_schedule(tables[0],time_tables[0])
#         schedule_for_second_week = self.__tablecon.get_direction_schedule(tables[1],time_tables[1])
#         for directionschedule in schedule_for_first_week:
#             all_schedules.append(directionschedule)
#         for directionschedule in schedule_for_second_week:
#             all_schedules.append(directionschedule)
#         return all_schedules
#
#     def get_schedules_from_link(self,link:str):
#         page = self.get_page(link)
#         tables = self.__tablecon.get_subject_tables(page)
#         time_tables = self.__tablecon.get_time_table(page)
#
#         all_schedules = []
#         schedule_for_first_week = self.__tablecon.get_direction_schedule(tables[0],time_tables[0])
#         schedule_for_second_week = self.__tablecon.get_direction_schedule(tables[1],time_tables[1])
#         for directionschedule in schedule_for_first_week:
#             all_schedules.append(directionschedule)
#         for directionschedule in schedule_for_second_week:
#             all_schedules.append(directionschedule)
#         return all_schedules
#
#     def get_directions(self,department: int,training_form: int, level:int,course:int, term: int) -> list[str]:
#         page = self._get_schedule_page(department, training_form, level, course, term)
#         tables = self.__tablecon.get_subject_tables(page)
#         directions = self.__tablecon.get_names_of_all_directions(tables[0])
#         return directions
#
#     def get_schedule_links_for_department(self,department: int) -> list[str]:
#         page = self._get_page_of_list_schedule(department)
#         all_links = self._get_schedule_links_from_page(page)
#         return all_links