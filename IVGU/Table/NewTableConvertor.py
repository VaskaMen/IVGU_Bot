from bs4 import BeautifulSoup

from IVGU.ScheduleObject.Subject import Subject
from IVGU.Table.LineConvertor import LineConvertor


class NewTableConvertor(LineConvertor):
    def get_subject(self,subgroup: str,line:str,tbody) -> Subject:
        timecodes = self.get_time_codes(tbody)
        time = self.get_time(line,timecodes)
        name = self.get_name_of_lesson(line)
        type = self.get_type_of_subject(line)
        return Subject(time,name,type,subgroup)

    @staticmethod
    def get_time_codes(tbody:BeautifulSoup):
        all_times = BeautifulSoup(str(tbody), "html.parser").select('.text-bold.cell.text-center')
        time_codes = {}
        for i in all_times:
            time_codes[f"{i.get('data-time')}"] = i.text
        return time_codes