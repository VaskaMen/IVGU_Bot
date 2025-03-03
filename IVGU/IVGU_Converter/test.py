from IVGU.IVGU_Converter.IvguConverter import IvguConverter

con = IvguConverter()

inst = 113
departments = con.get_departments(inst)
print(departments)

institutes = con.get_institutes(2)
print(institutes)