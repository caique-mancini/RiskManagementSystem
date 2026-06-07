import streamlit as st
import sqlite3
from pathlib import Path

db_path = Path(__file__).parent.parent / "database" / "database.db"

st.title("Cadastro de Produto")

name = st.text_input("Nome")

version = st.text_input("Versão")

family = st.text_input("Família")

if st.button("Salvar"):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO product (name, version, family)
        VALUES (?, ?, ?)
    """, (name, version, family))

    conn.commit()
    conn.close()

    st.success("Produto cadastrado com sucesso!")

    st.subheader("Produtos cadastrados")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("SELECT * FROM product")

dados = cursor.fetchall()

conn.close()

st.dataframe(
    dados,
    use_container_width=True
)