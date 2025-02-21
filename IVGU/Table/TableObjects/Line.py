from bs4 import ResultSet, Tag, BeautifulSoup


class Line:
    @staticmethod
    def get_lines_of_subjects(table: str) -> ResultSet[Tag]:
        tbody = BeautifulSoup(table, "html.parser")
        tbody.find('thead').extract()
        tr = BeautifulSoup(str(tbody),'html.parser').select('tr:not(thead tr)')
        td = BeautifulSoup(str(tr),'html.parser').select('td')
        return td

    @staticmethod
    def lines_separator_into_cells(td: ResultSet[Tag]) -> ResultSet[Tag]:
        for id,elem in enumerate(td):
            colspan = elem.get("colspan")
            if colspan is not None:
                elem["colspan"] = ''
                for i in range(int(colspan)-1):
                    td.insert(id+i, elem)
        return td