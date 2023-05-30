import streamlit as st
import pandas as pd

# Criar um DataFrame vazio para armazenar os dados
dados_producao = pd.DataFrame(columns=['Dia', 'Produto', 'Quantidade', 'Defeitos'])

while True:
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Selecione uma opção:", ("Registrar produção", "Registrar defeitos", "Mostrar estatísticas"))

    if opcao == "Registrar produção":
        dia = st.text_input("Digite o dia da produção:")
        produto = st.text_input("Digite o produto:")
        quantidade = st.number_input("Digite a quantidade produzida:", min_value=0, value=0, step=1)

        dados_producao = dados_producao.append({
            'Dia': dia,
            'Produto': produto,
            'Quantidade': quantidade,
            'Defeitos': 0
        }, ignore_index=True)

    elif opcao == "Registrar defeitos":
        dia = st.text_input("Digite o dia em que ocorreu o defeito:")
        produto = st.text_input("Digite o produto com defeito:")
        defeitos = st.number_input("Digite a quantidade de defeitos:", min_value=0, value=0, step=1)

        # Atualizar o número de defeitos para o produto e dia correspondentes
        dados_producao.loc[(dados_producao['Dia'] == dia) & (dados_producao['Produto'] == produto), 'Defeitos'] += defeitos

    elif opcao == "Mostrar estatísticas":
        # Mostrar as estatísticas
        st.subheader("Estatísticas")
        st.write("Peça com maior índice de reprovação:")
        st.write(dados_producao.groupby('Produto')['Defeitos'].sum().idxmax())
        st.write("Peça com maior quantidade de produção:")
        st.write(dados_producao.groupby('Produto')['Quantidade'].sum().idxmax())
        st.write("Média de erros semanais:")
        st.write(dados_producao['Defeitos'].mean())

    if not st.sidebar.button("Continuar"):
        break

# Salvar os dados em uma planilha Excel
dados_producao.to_excel('dados_producao.xlsx', index=False)
