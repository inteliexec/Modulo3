import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from config.config import set_page_config
set_page_config()

url = "https://docs.google.com/spreadsheets/d/1yVbOkuSSZ_oH7OKicOGclJHTKjORkoKt03jIFaEJCHk/edit?usp=sharing"


def sheets_connection():
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url)
    return data

# botão de atualização
st.write("Não encontrou sua empresa? Clique aqui para atualizar a lista de empresas")
update = st.button("Atualizar")
if update:
    st.cache_data.clear()

data = sheets_connection()
company = st.selectbox("Qual o nome da sua empresa?", data.columns, index=None)
st.session_state['company'] = company
if company != None:
                row = data[company].unique()
                name = st.selectbox("Qual o seu nome?", pd.Series(row).dropna().values, index=None)
                st.session_state['name'] = name

if company != None and name != None:
    st.write(f"Olá, {name} da empresa {company}! Prossiga para as próximas etapas no menu lateral.")