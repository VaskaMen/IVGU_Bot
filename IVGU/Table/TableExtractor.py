from bs4 import BeautifulSoup, ResultSet, Tag


class TableExtractor:
    @staticmethod
    def get_time_table(page:str) -> ResultSet[Tag]:
        time_tables = BeautifulSoup(page, 'html.parser').select('.first-table')
        return time_tables

    @staticmethod
    def get_time_codes(tbody:ResultSet[Tag]) -> dict[str,str]:
        all_times = BeautifulSoup(str(tbody), "html.parser").select('.text-bold.cell.text-center')
        time_codes = {}
        for i in all_times:
            time_codes[f"{i.get('data-time')}"] = i.text
        return time_codes

    @staticmethod
    def get_subject_tables(page:str) ->ResultSet[Tag]:
        subject_tables = BeautifulSoup(page, 'html.parser').select('.second-table')
        return subject_tables