import streamlit as st
import pandas as pd

# Definir o nome do arquivo xlsx
nome_arquivo = "nome_arquivo"

# Verificar se o arquivo existe, caso contrário criar um DataFrame vazio
try:
    df = pd.read_excel(nome_arquivo)
except FileNotFoundError:
    df = pd.DataFrame(columns=["product_name", "producao", "defeitos"])

# Módulo 1: Entrada de dados
st.header("Módulo 1: Entrada de dados")
product_name = st.text_input("Digite o nome do produto:")
producao = st.number_input("Digite a quantidade de produção:", min_value=0, step=1)

# Botões para salvar, limpar a base e avançar para o próximo módulo
salvar_button = st.button("Salvar")
limpar_button = st.button("Limpar base")
proximo_button = st.button("Próximo")

# Lógica para os botões
if salvar_button:
    # Verificar se o product_name já existe no DataFrame
    if product_name in df["product_name"].values:
        # Atualizar a linha correspondente ao product_name
        df.loc[df["product_name"] == product_name, ["producao"]] = producao
    else:
        # Criar uma nova linha no DataFrame
        nova_linha = pd.DataFrame([[product_name, producao, None]], columns=df.columns)
        df = pd.concat([df, nova_linha], ignore_index=True)
    # Salvar o DataFrame no arquivo xlsx
    df.to_excel(nome_arquivo, index=False)
    st.success("Informações salvas com sucesso!")

if limpar_button:
    # Limpar todas as informações do DataFrame e do arquivo xlsx
    df = pd.DataFrame(columns=["product_name", "producao", "defeitos"])
    df.to_excel(nome_arquivo, index=False)
    st.warning("Base de dados limpa!")

if proximo_button:
    # Avançar para o próximo módulo
    st.header("Módulo 2: Outras funcionalidades...")
    # Adicione o código para o próximo módulo aqui
