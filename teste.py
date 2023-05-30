import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuração das credenciais do Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Abre o arquivo do Google Sheets
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/11JG59DIymO3f7B1ZQU39k0xtGMMCPDI9/edit?usp=sharing'
gc = client.open_by_url(spreadsheet_url)
worksheet = gc.sheet1

# Criação de um DataFrame vazio para armazenar os dados
df_dados_producao = pd.DataFrame(columns=['Produto', 'Quantidade', 'Defeitos'])

# Menu lateral com as segmentações
opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"))

# Função para salvar os dados no Google Sheets
def salvar_dados(produto, quantidade, defeitos):
    nova_linha = [produto, quantidade, defeitos]
    worksheet.append_row(nova_linha)

# Segmentação "Registrar produção"
if opcao == "Registrar produção":
    st.header("Registrar Produção")
    produto = st.text_input("Nome do produto")
    quantidade = st.number_input("Quantidade de peças produzidas", min_value=0)
    if st.button("Salvar"):
        salvar_dados(produto, quantidade, 0)
        st.success("Dados salvos com sucesso!")

# Segmentação "Registrar defeitos"
elif opcao == "Registrar defeitos":
    st.header("Registrar Defeitos")
    produto = st.text_input("Nome do produto")
    defeitos = st.number_input("Quantidade de peças defeituosas", min_value=0)
    if st.button("Salvar"):
        salvar_dados(produto, 0, defeitos)
        st.success("Dados salvos com sucesso!")

# Segmentação "Mostrar estatísticas"
elif opcao == "Mostrar estatísticas":
    st.header("Estatísticas")
    df_dados_producao = pd.DataFrame(worksheet.get_all_records())
    st.dataframe(df_dados_producao)

# Botão para zerar os dados
if st.button("Zerar Dados"):
    worksheet.clear()
    st.success("Dados zerados com sucesso!")
