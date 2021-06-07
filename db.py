import sqlite3

connection = sqlite3.connect('./database/data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
#cursor.execute(create_table)

users = [
    (2, 'yassine2', 'rfg'),
    (3, 'yassine3', 'xyz'),
    (4, 'yassine4', 'xyzg')
]

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
for user in users:
    cursor.execute(insert_query, user)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)
connection.commit()
connection.close()