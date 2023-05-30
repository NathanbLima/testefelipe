import pandas as pd

# Criar um DataFrame vazio para armazenar os dados
dados_producao = pd.DataFrame(columns=['Dia', 'Produto', 'Quantidade', 'Defeitos'])

while True:
    print("========== MENU ==========")
    print("1 - Registrar produção")
    print("2 - Registrar defeitos")
    print("3 - Mostrar estatísticas")
    print("0 - Sair")
    opcao = input("Selecione uma opção: ")

    if opcao == '1':
        dia = input("Digite o dia da produção: ")
        produto = input("Digite o produto: ")
        quantidade = int(input("Digite a quantidade produzida: "))

        dados_producao = dados_producao.append({
            'Dia': dia,
            'Produto': produto,
            'Quantidade': quantidade,
            'Defeitos': 0
        }, ignore_index=True)

    elif opcao == '2':
        dia = input("Digite o dia em que ocorreu o defeito: ")
        produto = input("Digite o produto com defeito: ")
        defeitos = int(input("Digite a quantidade de defeitos: "))

        # Atualizar o número de defeitos para o produto e dia correspondentes
        dados_producao.loc[(dados_producao['Dia'] == dia) & (dados_producao['Produto'] == produto), 'Defeitos'] += defeitos

    elif opcao == '3':
        # Mostrar as estatísticas
        print("======== Estatísticas ========")
        print("Peça com maior índice de reprovação:")
        print(dados_producao.groupby('Produto')['Defeitos'].sum().idxmax())
        print("Peça com maior quantidade de produção:")
        print(dados_producao.groupby('Produto')['Quantidade'].sum().idxmax())
        print("Média de erros semanais:")
        print(dados_producao['Defeitos'].mean())

    elif opcao == '0':
        break

# Salvar os dados em uma planilha Excel
dados_producao.to_excel('dados_producao.xlsx', index=False)
