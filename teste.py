import streamlit as st
import pandas as pd

# Criar uma lista vazia para armazenar os dados
dados_producao = []

while True:
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"))

    if opcao == "Registrar produção":
        produto = st.text_input("Digite o produto:")
        quantidade = st.number_input("Digite a quantidade produzida:", min_value=0, value=0, step=1)

        dados_producao.append({
            'Produto': produto,
            'Quantidade': quantidade,
            'Defeitos': 0
        })

    elif opcao == "Registrar defeitos":
        produto = st.text_input("Digite o produto com defeito:")
        defeitos = st.number_input("Digite a quantidade de defeitos:", min_value=0, value=0, step=1)

        # Atualizar o número de defeitos para o produto correspondente
        for item in dados_producao:
            if item['Produto'] == produto:
                item['Defeitos'] += defeitos

    elif opcao == "Mostrar estatísticas":
        # Converter a lista de dados para DataFrame
        df_dados_producao = pd.DataFrame(dados_producao)

        # Mostrar as estatísticas
        st.subheader("Estatísticas")
        st.write("Peça com maior índice de reprovação:")
        st.write(df_dados_producao.groupby('Produto')['Defeitos'].sum().idxmax())
        st.write("Peça com maior quantidade de produção:")
        st.write(df_dados_producao.groupby('Produto')['Quantidade'].sum().idxmax())
        st.write("Média de erros semanais:")
        st.write(df_dados_producao['Defeitos'].mean())

    if not st.sidebar.button("Continuar"):
        break

# Salvar os dados em uma planilha Excel
df_dados_producao = pd.DataFrame(dados_producao)
df_dados_producao.to_excel('dados_producao.xlsx', index=False)
