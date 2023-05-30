import streamlit as st
import pandas as pd

# Função para ler o arquivo xlsx ou criar um novo DataFrame vazio
def ler_dados_producao():
    try:
        df = pd.read_excel('dados_producao.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Produto', 'Quantidade', 'Defeitos'])
    return df

# Função para salvar os dados no arquivo xlsx
def salvar_dados_producao(df):
    df.to_excel('dados_producao.xlsx', index=False)

# Carrega os dados de produção
df_dados_producao = ler_dados_producao()

# Menu lateral
opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"))

if opcao == "Registrar produção":
    st.header("Registrar produção")
    produto = st.text_input("Nome do produto (chave única)")
    quantidade = st.number_input("Quantidade de peças produzidas", min_value=0)
    
    if st.button("Salvar"):
        # Verifica se o nome do produto já existe no DataFrame
        if produto in df_dados_producao['Produto'].values:
            # Atualiza a linha correspondente
            df_dados_producao.loc[df_dados_producao['Produto'] == produto, 'Quantidade'] = quantidade
        else:
            # Cria um novo DataFrame com os dados atualizados
            novo_dados = {'Produto': [produto], 'Quantidade': [quantidade], 'Defeitos': [0]}
            df_dados_producao = pd.concat([df_dados_producao, pd.DataFrame(novo_dados)], ignore_index=True)
        
        # Salva os dados no arquivo xlsx
        salvar_dados_producao(df_dados_producao)

        st.success("Informações salvas com sucesso!")

elif opcao == "Registrar defeitos":
    st.header("Registrar defeitos")
    # Código para registrar defeitos

elif opcao == "Mostrar estatísticas":
    st.header("Mostrar estatísticas")
    # Código para mostrar estatísticas
