import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM product")

dados = cursor.fetchall()

for linha in dados:
    print(linha)

conn.close()