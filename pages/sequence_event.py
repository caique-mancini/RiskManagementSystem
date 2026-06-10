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