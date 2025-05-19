import requests

class IVGUAuthorisation:
    __user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    _session = requests.Session()
    __csrf: str = ""

    def __init__(self,email: str,password: str):
        self.login(email,password)

    def __get_csrf(self) -> str:
        self._session.get("https://uni.ivanovo.ac.ru", headers={
            'User-Agent': self.__user_agent_val
        })
        _csrf = self._session.cookies.get('csrf', domain="uni.ivanovo.ac.ru")
        return _csrf

    def login(self, email: str, password:str):
        self.__csrf = self.__get_csrf()
        h = {
            "csrf": self.__csrf,
            "email": email,
            "password": password,
            "authorization": ''
        }
        self._session.post("https://uni.ivanovo.ac.ru/auth/", h)
