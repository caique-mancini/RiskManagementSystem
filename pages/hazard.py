import streamlit as st
import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / "database" / "database.db"

st.title("Hazard Registration")

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

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO hazard
    (product_id, hazard_category, hazard_description)
    VALUES (?, ?, ?)
    """,
    (
        produto_escolhido[0],
        hazard_category,
        hazard_description
    ))

    conn.commit()

    conn.close()

    st.success("Hazard cadastrado com sucesso!")

    st.subheader("Hazards cadastrados")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM hazard
""")

dados = cursor.fetchall()

conn.close()

st.dataframe(dados)