from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB

sql = SQLDBB()
api = APIIVGU("miha2204n@gmail.com","8azr25pb")
sh = api.get_schedule(118,6,1,2,2)
for s in sh:
    sql.add_direction_schedule(s, 129)