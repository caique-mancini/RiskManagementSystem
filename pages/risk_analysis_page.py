import sqlite3
from datetime import datetime

# Criar conexão com banco de dados
def create_database():
    conn = sqlite3.connect('risk_management.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS risk_analysis (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
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
    ''')
    
    conn.commit()
    conn.close()

# Executar criação do banco de dados
if __name__ == "__main__":
    create_database()
    print("Banco de dados criado com sucesso!")
