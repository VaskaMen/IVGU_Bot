import requests


class StaticIVGUPage:

    @staticmethod
    def get_schedule_institute_page():
        return requests.get("https://ivanovo.ac.ru/students/schedule/").text

    @staticmethod
    def get_page(institute_schedule: str = ""):
        return requests.get(f"https://ivanovo.ac.ru/{institute_schedule}")


