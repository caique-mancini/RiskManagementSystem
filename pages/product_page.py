import streamlit as st

st.title("Cadastro de Produto")

name = st.text_input("Nome")

version = st.text_input("Versão")

family = st.text_input("Família")

if st.button("Salvar"):
    st.success("Botão funcionando!")