from datetime import datetime, date


class DateFunctions:

    def check_date_format(self, message: str):
        message1 = self.__remove_extra_space(message)
        split_message = message1.split(" ")
        return (self.__check_day_format(split_message[0])
                and self.__check_month(split_message[1]))\
                and self.__check_year(split_message[2])


    @staticmethod
    def __check_day_format(day: str) -> bool:
       return day.isdigit() and 0 < int(day) < 31

    @staticmethod
    def __remove_extra_space(message: str) -> str:
        message_1 = message
        while "  " in message_1:
           message_1 = message_1.replace("  "," ")
        return message_1

    @staticmethod
    def __check_month(month: str) -> bool:
        months = ["января", " января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября","октября", "ноября", "декабря"]
        return month in months

    @staticmethod
    def __check_year(year: str) -> bool:
        return year.isdigit() and int(year) > 2000

    @staticmethod
    def convert_str_to_date(str_date: str) -> date:
        month_mapping = {
            "января": 1,
            "февраля": 2,
            "марта": 3,
            "апреля": 4,
            "мая": 5,
            "июня": 6,
            "июля": 7,
            "августа": 8,
            "сентября": 9,
            "октября": 10,
            "ноября": 11,
            "декабря": 12
        }
        split = str_date.split(" ")
        day = split[0]
        month_name = split[1]
        year = split[2]
        month = month_mapping[month_name.lower()]

        date_obj = datetime(int(year), month, int(day))
        return date_obj.date()

    def get_actual_dates(self,dates: list[str]) -> list[str]:
        actual_dates = []
        month_mapping = {
            "01": "января",
            "02": "февраля",
            "03": "марта",
            "04": "апреля",
            "05": "мая",
            "06": "июня",
            "07": "июля",
            "08": "августа",
            "09": "сентября",
            "10": "октября",
            "11": "ноября",
            "12": "декабря"
        }
        week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        for date in dates:
            weekday = week[self.convert_date_str_to_date(date).weekday()]
            splitted = date.split('-')
            day = int(splitted[2])
            month = month_mapping[splitted[1]]
            year = splitted[0]
            new_date = str(day) + " " + month + " " + year + " " + weekday
            actual_dates.append(new_date)
        return actual_dates

    @staticmethod
    def convert_date_str_to_date(s: str) -> date:
        return datetime.strptime(s.split(' ')[0], '%Y-%m-%d').date()