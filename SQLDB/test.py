from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB

sql = SQLDBB()
api = APIIVGU("miha2204n@gmail.com","8azr25pb")


print(api.get_departments(116))