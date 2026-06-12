import streamlit as st
import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / "database" / "database.db"

st.title("Cadastro de Sequence Event")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
SELECT hazard_id, hazard_description
FROM hazard
""")

hazards = cursor.fetchall()
conn.close()

hazard_escolhido = st.selectbox(
    "Hazard",
    hazards,
    format_func=lambda x: x[1]
)

event_order = st.number_input(
    "Ordem do Evento",
    min_value=1,
    step=1
)

description_sequence = st.text_input(
    "Descrição do Evento"
)

if st.button("Salvar"):

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sequence_event
    (hazard_id, event_order, description_sequence)
    VALUES (?, ?, ?)
    """,
    (
        hazard_escolhido[0],
        event_order,
        description_sequence
    ))

    conn.commit()

    conn.close()

st.success("Sequence Event cadastrado com sucesso!")

# aqui inseri um join para trazer o nome do hazard e nao o ID.

st.subheader("Sequence Events cadastrados")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
SELECT 
    sequence_event.sequence_id,
    hazard.hazard_description,
    sequence_event.event_order,
    sequence_event.description_sequence
FROM sequence_event
JOIN hazard
ON sequence_event.hazard_id = hazard.hazard_id
""")

dados = cursor.fetchall()

conn.close()

st.dataframe(dados)