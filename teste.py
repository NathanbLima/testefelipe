import streamlit as st
import pandas as pd

# Carrega os dados de produção a partir do arquivo Excel ou cria um novo DataFrame vazio
try:
    producao_df = pd.read_excel('dados_producao.xlsx')
except FileNotFoundError:
    producao_df = pd.DataFrame(columns=['Produto', 'Quantidade', 'Defeitos'])

# Função para salvar os dados de produção no arquivo Excel
def salvar_dados_producao():
    producao_df.to_excel('dados_producao.xlsx', index=False)

# Função para registrar a produção
def registrar_producao():
    produto = st.text_input("Digite o nome do produto:")
    quantidade = st.number_input("Digite a quantidade produzida:", min_value=0, step=1, value=0)

    # Verifica se o produto já existe no DataFrame
    if produto in producao_df['Produto'].values:
        # Atualiza a quantidade de produção
        producao_df.loc[producao_df['Produto'] == produto, 'Quantidade'] += quantidade
    else:
        # Adiciona uma nova linha para o produto
        novo_produto = {'Produto': produto, 'Quantidade': quantidade, 'Defeitos': 0}
        producao_df = producao_df.append(novo_produto, ignore_index=True)

    # Salva os dados atualizados no arquivo Excel
    salvar_dados_producao()

# Função para registrar os defeitos
def registrar_defeitos():
    produto = st.text_input("Digite o nome do produto:")
    defeitos = st.number_input("Digite a quantidade de defeitos:", min_value=0, step=1, value=0)

    # Atualiza a quantidade de defeitos para o produto selecionado
    producao_df.loc[producao_df['Produto'] == produto, 'Defeitos'] += defeitos

    # Salva os dados atualizados no arquivo Excel
    salvar_dados_producao()

# Função para exibir os dados de produção e informações adicionais
def exibir_dados_producao():
    st.subheader("Dados de Produção")
    st.write(producao_df)

    # Converte a coluna "Defeitos" para o tipo numérico
    producao_df['Defeitos'] = pd.to_numeric(producao_df['Defeitos'])

    produto_reprovacao_semanal = producao_df.loc[producao_df['Defeitos'].idxmax(), 'Produto']
    produto_maior_producao = producao_df.loc[producao_df['Quantidade'].idxmax(), 'Produto']
    media_erros_semanais = producao_df['Defeitos'].mean()

    st.subheader("Informações para Apoio a Decisões")
    st.write("Peça com maior índice de reprovação semanal:", produto_reprovacao_semanal)
    st.write("Peça com maior quantidade de produção:", produto_maior_producao)
    st.write("Média de erros semanais:", media_erros_semanais)

# Configurações iniciais
st.set_page_config(page_title="Análise de Produção", layout="wide")

# Título e descrição
st.title("Análise de Produção")
st.write("Este programa permite registrar e analisar os dados de produção.")

# Menu de interações
opcoes_menu = ["Registrar Produção", "Registrar Defeitos", "Visualizar Dados"]
escolha = st.sidebar.selectbox("Selecione uma opção:", opcoes_menu)

# Realiza a ação com base na escolha do usuário
if escolha == "Registrar Produção":
    registrar_producao()
elif escolha == "Registrar Defeitos":
    registrar_defeitos()
elif escolha == "Visualizar Dados":
    exibir_dados_producao()
