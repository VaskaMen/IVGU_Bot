import re
from datetime import datetime, date


class BotFunctions:
    @staticmethod
    def check_date_format(s: str):
        if re.compile(r'\d\d\d\d-\d\d-\d\d').match(s):
            return True
        else:
            return False

    @staticmethod
    def convert_str_to_date(s: str) -> date:
        return datetime.strptime(s.split(' ')[0], '%Y-%m-%d').date()