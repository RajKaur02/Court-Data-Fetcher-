import sqlite3

conn = sqlite3.connect("db_logger.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM queries ORDER BY id DESC")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
