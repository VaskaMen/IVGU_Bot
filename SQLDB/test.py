import sqlite3

from SQLDB.SQLCommands.CreateCommands import CreateCommands

con = sqlite3.connect("lesson.db")
cur = con.cursor()

cur.execute(CreateCommands.create_table_levels())

cur.execute(CreateCommands.create_table_departments())

cur.execute(CreateCommands.create_table_groups())

cur.execute(CreateCommands.create_table_places())

cur.execute(CreateCommands.create_table_lessons())

cur.execute(CreateCommands.create_table_directions())

cur.execute(CreateCommands.create_table_subgroups())

cur.execute(CreateCommands.create_table_subjects())

cur.execute(CreateCommands.create_table_teachers())

cur.execute(CreateCommands.create_table_teachers_lesson())

con.commit()