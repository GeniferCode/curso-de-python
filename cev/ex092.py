from datetime import date

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem):'))
if dados['ctps'] != 0:
    dados['Contratacao'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Contratacao'] + 35) - date.today().year + dados['idade']
print('-=-' * 10)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
