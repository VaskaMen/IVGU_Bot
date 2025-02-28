from IVGU.IVGU_Converter.IvguConverter import IvguConverter
from JsonDB.DepartmentsDB import DepartmentsDB

con = IvguConverter()
depdb = DepartmentsDB("departments.json")

inst = 113
all_tags = con.get_tags_departments(inst)
departments = con.get_departments(all_tags)

depdb.add_departments(departments)
# print(con.get_departments(all_tags))
