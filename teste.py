import streamlit as st
import pandas as pd

# Criar um DataFrame vazio para armazenar os dados
df_dados_producao = pd.DataFrame(columns=['Produto', 'Quantidade', 'Defeitos'])

while True:
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"), key="menu_opcao")

    if opcao == "Registrar produção":
        produto = st.text_input("Digite o produto:", key="produto")
        quantidade = st.number_input("Digite a quantidade produzida:", min_value=0, value=0, step=1, key="quantidade")

        df_dados_producao = df_dados_producao.append({
            'Produto': produto,
            'Quantidade': quantidade,
            'Defeitos': 0
        }, ignore_index=True)

    elif opcao == "Registrar defeitos":
        produto = st.text_input("Digite o produto com defeito:", key="produto_defeito")
        defeitos = st.number_input("Digite a quantidade de defeitos:", min_value=0, value=0, step=1, key="quantidade_defeitos")

        # Atualizar o número de defeitos para o produto correspondente
        df_dados_producao.loc[df_dados_producao['Produto'] == produto, 'Defeitos'] += defeitos

    elif opcao == "Mostrar estatísticas":
        if df_dados_producao.empty:
            st.warning("Nenhum dado de produção registrado.")
        else:
            st.subheader("Estatísticas")
            st.write("Peça com maior índice de reprovação:")
            st.write(df_dados_producao.groupby('Produto')['Defeitos'].sum().idxmax())
            st.write("Peça com maior quantidade de produção:")
            st.write(df_dados_producao.groupby('Produto')['Quantidade'].sum().idxmax())
            st.write("Média de erros semanais:")
            st.write(df_dados_producao['Defeitos'].mean())

    if not st.sidebar.button("Continuar", key="continuar"):
        break

# Salvar os dados em uma planilha Excel
df_dados_producao.to_excel('dados_producao.xlsx', index=False)
