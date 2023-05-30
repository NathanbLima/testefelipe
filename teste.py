import streamlit as st
import pandas as pd

# Definir o nome do arquivo xlsx
nome_arquivo = "dados.xlsx"

# Verificar se o arquivo existe, caso contrário criar um DataFrame vazio
try:
    df = pd.read_excel(nome_arquivo)
except FileNotFoundError:
    df = pd.DataFrame(columns=["product_name", "producao", "defeitos"])

# Definir o layout da página com o menu lateral
st.set_page_config(layout="wide")

# Módulo 1: Entrada de dados
with st.sidebar:
    st.header("Módulo 1: Entrada de dados")
    product_name = st.text_input("Digite o nome do produto:")
    producao = st.number_input("Digite a quantidade de produção:", min_value=0, step=1)
    salvar_button = st.button("Salvar")
    limpar_button = st.button("Limpar base")

# Lógica para os botões do módulo 1
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
    st.sidebar.success("Informações salvas com sucesso!")

if limpar_button:
    # Limpar todas as informações do DataFrame e do arquivo xlsx
    df = pd.DataFrame(columns=["product_name", "producao", "defeitos"])
    df.to_excel(nome_arquivo, index=False)
    st.sidebar.warning("Base de dados limpa!")

# Módulo 2: Entrada de defeitos
with st.sidebar:
    st.header("Módulo 2: Entrada de defeitos")
    product_name_defeitos = st.text_input("Digite o nome do produto:")
    defeitos = st.number_input("Digite a quantidade de defeitos:", min_value=0, step=1)
    salvar_button_defeitos = st.button("Salvar")
    limpar_button_defeitos = st.button("Limpar base")

# Lógica para os botões do módulo 2
if salvar_button_defeitos:
    # Verificar se o product_name já existe no DataFrame
    if product_name_defeitos in df["product_name"].values:
        # Atualizar a linha correspondente ao product_name
        df.loc[df["product_name"] == product_name_defeitos, ["defeitos"]] = defeitos
    else:
        # Criar uma nova linha no DataFrame
        nova_linha = pd.DataFrame([[product_name_defeitos, None, defeitos]], columns=df.columns)
        df = pd.concat([df, nova_linha], ignore_index=True)
    # Salvar o DataFrame no arquivo xlsx
    df.to_excel(nome_arquivo, index=False)
    st.sidebar.success("Informações de defeitos salvas com sucesso!")

if limpar_button_defeitos:
    # Limpar a coluna de defeitos do produto no DataFrame e no arquivo xlsx
    df.loc[df["product_name"] == product_name_defeitos, ["defeitos"]] = None
    df.to_excel(nome_arquivo, index=False)
    st.sidebar.warning("Informações de defeitos limpas!")

# Módulo 3: Estatísticas
with st.sidebar:
    st.header("Módulo 3: Estatísticas")
    # Cálculo da quantidade de erros em cada peça
    quantidade_erros = df["defeitos"].sum()
    st.write(f"Quantidade total de erros: {quantidade_erros}")
    
    # Acompanhamento da peça que apresenta maior índice de reprovação semanal
    maior_indice_reprovacao = df.loc[df["defeitos"].idxmax(), "product_name"]
    st.write(f"Peca com maior indice de reprovação semanal: {maior_indice_reprovacao}")
    
    # Acompanhamento da peça que apresenta maior quantidade de produção
    maior_quantidade_producao = df.loc[df["producao"].idxmax(), "product_name"]
    st.write(f"Peca com maior quantidade de produção: {maior_quantidade_producao}")
    
    # Acompanhamento da média de erros semanais
    media_erros_semanais = df["defeitos"].mean()
    st.write(f"Média de erros semanais: {media_erros_semanais}")

# Exibir os módulos 1 e 2 na página
st.header("Módulo 1: Entrada de dados")
st.write("Digite o nome do produto:")
st.write("Digite a quantidade de produção:")
st.write("Botões: Salvar, Limpar base")

st.header("Módulo 2: Entrada de defeitos")
st.write("Digite o nome do produto:")
st.write("Digite a quantidade de defeitos:")
st.write("Botões: Salvar, Limpar base")

# Exibir o módulo 3 na página
st.header("Módulo 3: Estatísticas")
st.write("Quantidade total de erros:")
st.write("Peca com maior indice de reprovação semanal:")
st.write("Peca com maior quantidade de produção:")
st.write("Média de erros semanais:")
