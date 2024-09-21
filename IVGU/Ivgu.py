import requests
from bs4 import BeautifulSoup, ResultSet, PageElement

class Ivgu:
    user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    session = requests.Session()
    csrf: str = ""

    def __init__(self):
        self.csrf = self.__get_csrf()

    def __get_csrf(self) -> str:
        r = self.session.get("https://uni.ivanovo.ac.ru", headers={
            'User-Agent': self.user_agent_val
        })
        _csrf = self.session.cookies.get('csrf', domain="uni.ivanovo.ac.ru")
        return _csrf

    def login(self, email: str, password:str):
        h = {
            "csrf": self.csrf,
            "email": email,
            "password": password,
            "authorization": ''
        }
        self.session.post("https://uni.ivanovo.ac.ru/auth/", h)

    def get_schedule_page(self) -> str:
       return self.session.get('https://uni.ivanovo.ac.ru/student/schedule').text

    def get_schedule_lines(self, html_page) -> ResultSet[PageElement]:
        el = BeautifulSoup(html_page, 'html.parser').find_all('div',{'class': 'active-day'})
        return el

