import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    version TEXT,
    family TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS hazard (
    hazard_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    hazard_category TEXT,
    hazard_description TEXT,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
)
""")

conn.commit()
conn.close()

print("Tabelas criadas com sucesso!")
