from IVGU.APIIVGU import APIIVGU
from SQLDB.SQLDBB import SQLDBB

sql = SQLDBB()
# api = APIIVGU("miha2204n@gmail.com","8azr25pb")
#
#
# print(api.get_departments(116))

# list =sql._get_group_id('Центр русистики и международного образования',
#                             'Очная Форма обучения',
#                             'ДОП',
#                                1,
#                               'Направление 00.00.01 Дополнительные общеобразовательные программы, обеспечивающие подготовку иностранных граждан и лиц без гражданства к освоению профессиональных образовательных программ на русском языке',
#                               'Гуманитарное направление',
#                         "Без подгрупп")
# print(list)

new_list = sql.get_sql_workday(9,'2025-05-14')
print(new_list)