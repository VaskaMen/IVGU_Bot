from IVGU.IVGUPage import IVGUPage
from IVGU.IVGUConverter import IVGUConverter
from IVGU.Table.Table import Table


class APIIVGU(IVGUPage, IVGUConverter,Table):

    def get_schedule(self,department:int,
                        training_form: int,
                        level: int,
                        course: int,
                        term: int,):
        page =  self._get_schedule_page(department,training_form,level,course,term)
        return self.get_schedules_from_page(page)

    def get_departments(self,institute: int) -> dict[str, str]:
        page = self._get_page_of_departments(institute)
        all_departments = self._get_departments_from_page(page)
        return all_departments

    def get_institutes(self,university_number: int) -> dict[str, str]:
        page = self._get_page_of_institutes(university_number)
        all_institutes = self._get_institutes_from_page(page)
        return all_institutes

    def get_schedule_links_for_department(self,department: int) -> list[str]:
        page = self._get_page_of_list_schedule(department)
        all_links = self._get_schedule_links_from_page(page)
        return all_links