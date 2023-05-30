import streamlit as st
import pandas as pd

# Criação de um DataFrame vazio
df_dados_producao = pd.DataFrame(columns=['Produto', 'Quantidade', 'Defeitos'])

# Menu lateral com 3 segmentações
opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"))

# Segmentação "Registrar produção"
if opcao == "Registrar produção":
    st.subheader("Registrar produção")
    produto = st.text_input("Digite o nome do produto:")
    quantidade = st.number_input("Digite a quantidade de peças produzidas:", min_value=0, step=1)
    if st.button("Salvar"):
        df_dados_producao = df_dados_producao.append({
            'Produto': produto,
            'Quantidade': quantidade,
            'Defeitos': 0
        }, ignore_index=True)
        st.success("Dados de produção registrados com sucesso!")

# Segmentação "Registrar defeitos"
elif opcao == "Registrar defeitos":
    st.subheader("Registrar defeitos")
    produto = st.text_input("Digite o nome do produto:")
    defeitos = st.number_input("Digite a quantidade de peças defeituosas:", min_value=0, step=1)
    if st.button("Salvar"):
        if produto in df_dados_producao['Produto'].values:
            df_dados_producao.loc[df_dados_producao['Produto'] == produto, 'Defeitos'] += defeitos
            st.success("Dados de defeitos registrados com sucesso!")
        else:
            st.error("Produto não encontrado!")

# Segmentação "Mostrar estatísticas"
elif opcao == "Mostrar estatísticas":
    st.subheader("Estatísticas")
    st.write("Tabela de produção e defeitos por produto:")
    st.table(df_dados_producao)

# Exibir DataFrame atualizado
st.write("Dados de produção atualizados:")
st.write(df_dados_producao)
