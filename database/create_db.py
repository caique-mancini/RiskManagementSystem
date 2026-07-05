import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "database.db"

conn = sqlite3.connect(db_path)

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

cursor.execute("""
CREATE TABLE IF NOT EXISTS sequence_event (
    sequence_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hazard_id INTEGER NOT NULL,
    event_order INTEGER,
    description_sequence TEXT,
    FOREIGN KEY (hazard_id)
        REFERENCES hazard(hazard_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS risk_analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_perigo TEXT NOT NULL,
    parte_constituinte_funcional_primaria TEXT,
    etapa_funcional_primaria TEXT,
    caracteristica_chave TEXT,
    contribuicao_interacao_componentes TEXT,
    funcao_requerida TEXT,
    modo_falha_potencial TEXT,
    causas_potenciais_mecanismo_falha TEXT,
    sequencia_eventos TEXT,
    situacao_perigosa_potencial TEXT,
    situacao_perigosa_dano_potencial TEXT,
    severidade_dano TEXT,
    probabilidade_j_para_k TEXT,
    probabilidade_k_para_dano TEXT,
    probabilidade_ocorrencia_dano TEXT,
    nivel_risco_paciente TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Tabelas criadas com sucesso!")

#py database/create_db.py
#python database/create_db.py