import sqlite3
from pathlib import Path
import streamlit as st


db_path = Path(__file__).parent.parent / "database" / "database.db"


def create_table():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
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
        """
    )

    conn.commit()
    conn.close()


create_table()

st.title("Análise de Risco")
st.caption("Cadastro manual da análise de risco no formato FMEA")

with st.form("risk_analysis_form"):
    tipo_perigo = st.text_input("Tipo de perigo")
    parte_constituinte = st.text_input("Parte constitutiva / funcional primária")
    etapa_funcional = st.text_input("Etapa funcional primária")
    caracteristica_chave = st.text_input("Característica chave")
    contribuicao_interacao = st.text_area("Contribuição da interação dos componentes")
    funcao_requerida = st.text_area("Função requerida")
    modo_falha = st.text_area("Modo de falha potencial")
    causas_falha = st.text_area("Causas potenciais / mecanismo de falha")
    sequencia_eventos = st.text_area("Sequência de eventos")
    situacao_perigosa_potencial = st.text_area("Situação perigosa potencial")
    situacao_perigosa_dano = st.text_area("Situação perigosa / dano potencial")
    severidade = st.text_input("Severidade do dano")
    probabilidade_j_para_k = st.text_input("Probabilidade J para K")
    probabilidade_k_para_dano = st.text_input("Probabilidade K para dano")
    probabilidade_ocorrencia = st.text_input("Probabilidade de ocorrência do dano")
    nivel_risco = st.text_input("Nível de risco do paciente")

    submitted = st.form_submit_button("Salvar análise")

    if submitted:
        if not tipo_perigo:
            st.warning("Preencha pelo menos o campo Tipo de perigo.")
        else:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO risk_analysis (
                    tipo_perigo,
                    parte_constituinte_funcional_primaria,
                    etapa_funcional_primaria,
                    caracteristica_chave,
                    contribuicao_interacao_componentes,
                    funcao_requerida,
                    modo_falha_potencial,
                    causas_potenciais_mecanismo_falha,
                    sequencia_eventos,
                    situacao_perigosa_potencial,
                    situacao_perigosa_dano_potencial,
                    severidade_dano,
                    probabilidade_j_para_k,
                    probabilidade_k_para_dano,
                    probabilidade_ocorrencia_dano,
                    nivel_risco_paciente
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    tipo_perigo,
                    parte_constituinte,
                    etapa_funcional,
                    caracteristica_chave,
                    contribuicao_interacao,
                    funcao_requerida,
                    modo_falha,
                    causas_falha,
                    sequencia_eventos,
                    situacao_perigosa_potencial,
                    situacao_perigosa_dano,
                    severidade,
                    probabilidade_j_para_k,
                    probabilidade_k_para_dano,
                    probabilidade_ocorrencia,
                    nivel_risco,
                ),
            )
            conn.commit()
            conn.close()
            st.success("Análise de risco cadastrada com sucesso!")

st.subheader("Análises cadastradas")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT * FROM risk_analysis ORDER BY id DESC")
dados = cursor.fetchall()
conn.close()

if dados:
    st.dataframe(dados, use_container_width=True)
else:
    st.info("Nenhuma análise de risco cadastrada ainda.")
