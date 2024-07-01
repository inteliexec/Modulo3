import streamlit as st
import pandas as pd
import io
import os
from PIL import Image

st.set_page_config(
    page_title="Inteli | Teste de modelos",
    page_icon=Image.open(os.path.join('assets', 'inteli_logo.png')),
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "mailto:Alessandro.Gagliardi@br.experian.com",
        "About": """Página construída para curso de dados do Inteli (2023)"""
    }
)

st.markdown(
                """
                <style>
                [data-testid="stElementToolbar"] {
                    display: none;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

def to_excel(df):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.close()
        processed_data = output.getvalue()
        return processed_data
    
if  st.session_state.get('is_fit') is None:
    st.write("Você precisa treinar um modelo antes")
    st.write("### Importante! \n As features devem ser *exatamente* as mesmas usadas para treino")
else:
    if st.session_state['is_fit']:
        st.write("# Aplicar score na base de teste")
        val = st.file_uploader("Envie seu arquivo para teste", type=['xlsx'], accept_multiple_files=False)
        if val is not None:
            model = st.session_state['model']
            df_val = pd.read_excel(val)
            X_val = df_val[st.session_state['features']]
            df_pred = X_val.copy()
            df_pred['Prediction'] = model.predict_proba(X_val)[:,1]
            st.download_button(
                label="Baixar dados",
                data=to_excel(df_pred),
                file_name="base_scorada.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.dataframe(df_pred.head(30))

