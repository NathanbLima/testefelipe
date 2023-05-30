import streamlit as st
import pandas as pd

# URL do Google Sheets público
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/11JG59DIymO3f7B1ZQU39k0xtGMMCPDI9/edit#gid=2069898541'

# Criação de um DataFrame vazio para armazenar os dados
df_dados_producao = pd.DataFrame(columns=['Produto', 'Quantidade', 'Defeitos'])

# Menu lateral com as segmentações
opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"))

# Função para salvar os dados no Google Sheets
def salvar_dados(produto, quantidade, defeitos):
    novo_dados = {'Produto': produto, 'Quantidade': quantidade, 'Defeitos': defeitos}
    df_dados_producao.loc[len(df_dados_producao)] = novo_dados

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
    df_dados_producao = pd.read_csv(spreadsheet_url)
    st.dataframe(df_dados_producao)

# Botão para zerar os dados
if st.button("Zerar Dados"):
    df_dados_producao = pd.DataFrame(columns=['Produto', 'Quantidade', 'Defeitos'])
    st.success("Dados zerados com sucesso!")
