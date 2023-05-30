import streamlit as st
import pandas as pd

# Função para carregar os dados de produção do cache ou criar uma lista vazia
@st.cache
def carregar_dados_producao():
    return []

# Carrega os dados de produção
lista_dados_producao = carregar_dados_producao()

# Menu lateral com 3 segmentações
opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"))

# Segmentação "Registrar produção"
if opcao == "Registrar produção":
    st.subheader("Registrar produção")
    produto = st.text_input("Digite o nome do produto:")
    quantidade = st.number_input("Digite a quantidade de peças produzidas:", min_value=0, step=1)
    if st.button("Salvar"):
        lista_dados_producao.append({
            'Produto': produto,
            'Quantidade': quantidade,
            'Defeitos': 0
        })
        st.success("Dados de produção registrados com sucesso!")

# Segmentação "Registrar defeitos"
elif opcao == "Registrar defeitos":
    st.subheader("Registrar defeitos")
    produto = st.text_input("Digite o nome do produto:")
    defeitos = st.number_input("Digite a quantidade de peças defeituosas:", min_value=0, step=1)
    if st.button("Salvar"):
        produto_encontrado = False
        for item in lista_dados_producao:
            if item['Produto'] == produto:
                item['Defeitos'] += defeitos
                produto_encontrado = True
                break
        if produto_encontrado:
            st.success("Dados de defeitos registrados com sucesso!")
        else:
            st.error("Produto não encontrado!")

# Segmentação "Mostrar estatísticas"
elif opcao == "Mostrar estatísticas":
    st.subheader("Estatísticas")
    st.write("Tabela de produção e defeitos por produto:")
    df_dados_producao = pd.DataFrame(lista_dados_producao)
    st.table(df_dados_producao)

# Salva os dados de produção atualizados no cache
st.cache(func=carregar_dados_producao)(lista_dados_producao)

# Exibir DataFrame atualizado
st.write("Dados de produção atualizados:")
st.write(pd.DataFrame(lista_dados_producao))
