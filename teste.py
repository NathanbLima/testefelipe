import streamlit as st
import pandas as pd

# Função para atualizar os dados na planilha Excel
def atualizar_dados(nome, quantidade, defeitos):
    df = pd.DataFrame({'Nome': [nome], 'Quantidade': [quantidade], 'Defeitos': [defeitos]})

    try:
        # Tenta ler o arquivo existente
        df_existente = pd.read_excel('dados.xlsx')
        df = pd.concat([df_existente, df], ignore_index=True)
    except FileNotFoundError:
        pass

    # Salva os dados atualizados no arquivo Excel
    df.to_excel('dados.xlsx', index=False)

# Função para exibir as informações solicitadas
def exibir_informacoes():
    try:
        df = pd.read_excel('dados.xlsx')

        st.write('---')
        st.write('Informações da produção:')
        st.write(df)

        st.write('---')
        st.write('Peça com maior índice de reprovação:')
        peca_reprovada = df.loc[df['Defeitos'].idxmax()]
        st.write(peca_reprovada['Nome'], 'com', peca_reprovada['Defeitos'], 'defeitos')

        st.write('---')
        st.write('Peça com maior quantidade de produção:')
        peca_producao = df.loc[df['Quantidade'].idxmax()]
        st.write(peca_producao['Nome'], 'com', peca_producao['Quantidade'], 'peças produzidas')

        st.write('---')
        st.write('Média de erros semanais:')
        media_erros = df['Defeitos'].mean()
        st.write(media_erros)

    except FileNotFoundError:
        st.write('Nenhum dado disponível.')

# Configurações da aplicação Streamlit
st.title('Análise de Dados da Produção')
st.subheader('Modulo 1: Entrada de dados da produção')

nome_producao = st.text_input('Nome da peça produzida:')
quantidade_producao = st.number_input('Quantidade de peças produzidas:', min_value=0)

st.subheader('Modulo 2: Entrada de dados de defeitos')

nome_defeito = st.text_input('Nome da peça com defeito:')
quantidade_defeito = st.number_input('Quantidade de peças defeituosas:', min_value=0)

if st.button('Salvar'):
    atualizar_dados(nome_producao, quantidade_producao, quantidade_defeito)

st.write('---')

st.subheader('Modulo 3: Informações e análise')

exibir_informacoes()
