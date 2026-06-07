import streamlit as st
import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / "database" / "database.db"

st.title("Cadastro de Hazard")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
SELECT product_id, name
FROM product
""")

produtos = cursor.fetchall()

conn.close()

produto_escolhido = st.selectbox(
    "Produto",
    produtos,
    format_func=lambda x: x[1]
)

hazard_category = st.text_input("Categoria")

hazard_description = st.text_input("Descrição")

if st.button("Salvar"):
    st.success("Botão funcionando!")