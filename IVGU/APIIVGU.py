from IVGU.IVGUPage import IVGUPage
from IVGU.IVGUConverter import IVGUConverter


class APIIVGU(IVGUPage, IVGUConverter):

    def get_departments(self,institute: int) -> dict[str, str]:
        page = self._get_page_of_departments(institute)
        all_departments = self._get_departments_from_page(page)
        return all_departments

    def get_institutes(self,university_number: int) -> dict[str, str]:
        page = self._get_page_of_institutes(university_number)
        all_institutes = self._get_institutes_from_page(page)
        return all_institutes
