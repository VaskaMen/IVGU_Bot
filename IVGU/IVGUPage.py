from bs4 import BeautifulSoup, ResultSet, PageElement

from IVGU.IVGUAuthorisation import IVGUAuthorisation

class IVGUPage(IVGUAuthorisation):

    @staticmethod
    def get_schedule_lines(html_page) -> ResultSet[PageElement]:
        el = BeautifulSoup(html_page, 'html.parser').find_all('div',{'class': 'active-day'})
        return el

    def _get_schedule_page(self,
                           department:int,
                           training_form: int,
                           level: int,
                           course: int,
                           term: int,
                           ) -> str:
        return self._session.get(f'https://uni.ivanovo.ac.ru/info/showschedule/{department}/{training_form}/{level}/{course}/{term}').text

    def _get_page_of_departments(self,
                                 institute: int,
                                 ):
        return self._session.get(f"https://uni.ivanovo.ac.ru/info/institutes/{institute}").text

    def _get_page_of_institutes(self,
                                university_number: int,
                                ):
        return self._session.get(f"https://uni.ivanovo.ac.ru/info/university/{university_number}").text