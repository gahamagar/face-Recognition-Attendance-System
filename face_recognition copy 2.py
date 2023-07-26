import mysql.connector

conn = mysql.connector.connect(
    username='root',
    password='root',
    host='localhost',
    database='face_recognition',
    port=3306
)

cursor = conn.cursor()


query = "SELECT * FROM student"

cursor.execute(query)


rows = cursor.fetchall()


cursor.close()
conn.close()


for row in rows:
    print(row)
