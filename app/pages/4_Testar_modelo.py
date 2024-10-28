import streamlit as st
import pandas as pd
import io
import boto3
from urllib import parse
from config.config import set_page_config
set_page_config()

url = "https://docs.google.com/spreadsheets/d/1yVbOkuSSZ_oH7OKicOGclJHTKjORkoKt03jIFaEJCHk/edit?usp=sharing"

def to_excel(df):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.close()
        processed_data = output.getvalue()
        return processed_data

def upload_file_to_s3(df, file_name):
    tags = {"name": st.session_state['name'], "area": "default"}
    company = st.session_state['company']
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False, engine='openpyxl')
    excel_buffer.seek(0)
    s3_client = boto3.client('s3')
    s3_client.upload_fileobj(
        excel_buffer,
        Bucket='inteli-exec-bucket',
        Key=f'{company}/{file_name}.xlsx',
        ExtraArgs={"Tagging": parse.urlencode(tags)}
    )
    st.success('O upload do arquivo foi realizado com sucesso!', icon="✅")
    
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
            st.dataframe(df_pred.head(30))
            file_name = st.text_input("Para enviar o resultado do seu modelo para o professor, insira o nome que deseja para o arquivo:", "")
            if file_name != "":
                upload_button = st.button("Enviar para o professor")
                if upload_button:
                    upload_file_to_s3(df_pred, file_name)

