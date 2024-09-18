
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


class Ivgu:
    __chrome_options = Options()
    __chrome_options.add_argument("--headless")
    EdgeChromiumDriverManager().install()
    wd = webdriver.Edge(options=__chrome_options)
    
    
    def open_student_page(self):
        self.wd.get("https://uni.ivanovo.ac.ru/student/schedule")
        
    def login(self, email:str, password: str):
        self.wd.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/form/div[2]/div[1]/input').send_keys(email)
        self.wd.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/form/div[2]/div[2]/input').send_keys(password)
        self.wd.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/form/div[3]/button').click()
        
    def open_schedule(self):
        self.wd.get("https://uni.ivanovo.ac.ru/student/schedule")

    def get_schedule_lines(self) ->  list[WebElement]:
        el = self.wd.find_elements(by=By.CLASS_NAME, value='active-day')
        return el

    def close(self):
        self.wd.close()