import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd
import pygsheets

# URL do Google Sheets
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/11JG59DIymO3f7B1ZQU39k0xtGMMCPDI9/edit#gid=2069898541'

# Abrir o Google Sheets usando a URL
gc = pygsheets.authorize(service_file=None)

# Abrir a planilha
sh = gc.open_by_url(spreadsheet_url)

# Obter a planilha desejada
worksheet = sh.sheet1

# Obter os valores da planilha
dados = worksheet.get_all_values()

# Criar o DataFrame
df_dados_producao = pd.DataFrame(dados[1:], columns=dados[0])

# Exibir o DataFrame
st.dataframe(df_dados_producao)


# Segmentação "Mostrar estatísticas"
st.header("Estatísticas")
df_dados_producao = pd.read_csv(spreadsheet_url)
st.dataframe(df_dados_producao)

# Menu lateral com as segmentações
opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos"))

# Função para salvar os dados no Google Sheets
def salvar_dados(produto, quantidade, defeitos):
    nova_linha = {'Produto': produto, 'Quantidade': quantidade, 'Defeitos': defeitos}
    df_dados_producao = df_dados_producao.append(nova_linha, ignore_index=True)
    df_dados_producao.to_csv(spreadsheet_url, index=False)

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
