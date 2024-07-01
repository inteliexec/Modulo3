import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Inteli Exec",
    page_icon=Image.open(os.path.join('assets', 'inteli_logo.png')),
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image(Image.open(os.path.join('assets', 'inteli_logo_exec.png')))

st.write("# Inteli Exec - Treinamento de modelos de machine learning")

#st.sidebar.success("Selecione .")

st.markdown(
    """
    Esta página contém conteúdos específicos para o Módulo 3:
    
    * Dados para download
    * Interface para treino de modelos de machine learning

    Use o menu à esquerda para acessar as diferentes páginas.
"""
)