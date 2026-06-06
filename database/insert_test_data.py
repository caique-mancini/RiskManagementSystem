import sqlite3
conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO product (name, version, family) 
VALUES ('Bomba Infusão', '1.0', 'Equipamento')
""")

cursor.execute("""
INSERT INTO product (name, version, family) 
VALUES ('Placa lefort', '1.0', 'Implante')
""")  
    
conn.commit()
conn.close()

print("Dados inseridos com sucesso!")      