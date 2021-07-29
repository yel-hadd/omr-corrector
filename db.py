import sqlite3

connection = sqlite3.connect('./database/userdata.db')

cursor = connection.cursor()

create_table = "CREATE TABLE Users (id int )"
#cursor.execute(create_table)


cursor.execute()

connection.commit()
connection.close()