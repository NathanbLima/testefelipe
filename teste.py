import streamlit as st
import pandas as pd

# Configurações iniciais
st.set_page_config(page_title="Análise de Produção", layout="wide")

# Título do aplicativo
st.title("Análise de Produção")

# Entrada da quantidade de peças produzidas por dia
producao_dia = st.number_input("Quantidade de peças produzidas por dia:", min_value=0)

# Entrada da quantidade de defeitos ocorridos com escolha da peça defeituosa
defeitos = st.number_input("Quantidade de defeitos ocorridos:", min_value=0)
peca_defeituosa = st.selectbox("Escolha a peça ao qual o erro está sendo cadastrado:",
                               ["Peça A", "Peça B", "Peça C", "Peça D"])

# Armazenamento dos dados em um DataFrame
dados = pd.DataFrame({
    "Produção diária": [producao_dia],
    "Defeitos": [defeitos],
    "Peça defeituosa": [peca_defeituosa]
})

# Exibição dos dados na tela
st.subheader("Dados inseridos:")
st.write(dados)

# Cálculo e exibição das informações
st.subheader("Informações para apoio a decisões:")

# Peça com maior índice de reprovação
maior_reprovacao = dados.groupby("Peça defeituosa")["Defeitos"].sum().idxmax()
st.write("Peça com maior índice de reprovação:", maior_reprovacao)

# Peça com maior quantidade de produção
maior_producao = dados["Produção diária"].idxmax()
st.write("Peça com maior quantidade de produção:", peca_defeituosa[maior_producao])

# Média de erros semanais
media_erros = dados["Defeitos"].mean()
st.write("Média de erros semanais:", media_erros)

# Salvando os dados em uma planilha Excel
dados.to_excel("dados_producao.xlsx", index=False)
st.write("Dados salvos em 'dados_producao.xlsx'")

# Acompanhamento on-line
st.subheader("Acompanhamento on-line")
st.write("Acompanhe os dados e as informações em tempo real!")


