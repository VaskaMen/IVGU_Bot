from bs4 import BeautifulSoup, ResultSet, Tag


class TableExtractor:
    @staticmethod
    def get_time_table(page:str) -> ResultSet[Tag]:
        time_tables = BeautifulSoup(page, 'html.parser').select('.first-table')
        return time_tables

    @staticmethod
    def get_subject_tables(page:str) ->ResultSet[Tag]:
        subject_tables = BeautifulSoup(page, 'html.parser').select('.second-table')
        return subject_tables