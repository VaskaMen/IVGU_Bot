from SQLDB.SQLDBB import SQLDBB

sql = SQLDBB()

new_list = sql.get_actual_dates(9,'2025-05-14')
print(new_list)