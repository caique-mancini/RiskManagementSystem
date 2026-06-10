import streamlit as st
import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / "database" / "database.db"

st.title("Cadastro de Sequence Event")

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
