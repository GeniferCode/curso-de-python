dados = {}
lista = []
soma_idade = 0
while True:
    dados['nome'] = str(input('Nome: ')).capitalize()
    dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
    while dados['sexo'] not in 'MF':
        print(f'\033[31mERRO!\033[m Por favor, digite apenas F ou M')
        dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
    dados['idade'] = int(input('Idade '))
    lista.append(dados.copy())
    r = str(input('Quer continuar? [S/N] ')).upper()[0]
    while  r not in 'SN':
        print(f'\033[31mERRO!\033[m Responda apenas com S ou N')
        r = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if r == 'N':
        break
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for pessoa in lista:
    for k, v in pessoa.items():
        if k == 'idade':
            soma_idade += v
media = soma_idade / len(lista)
print(f'B) A média de idade é {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ')
for pessoa in lista:
    for k, v in pessoa.items():
        if pessoa['sexo'] == 'F':
            print(pessoa['nome'], end=' ')
            break
print('\nD) Lista das pessoas que estão acima da média: ')
for pessoa in lista:
    for k, v in pessoa.items():
        if pessoa['idade'] > media:
            print(f'   Nome = {pessoa['nome']}; Sexo = {pessoa['sexo']}; Idade = {pessoa['idade']}')
            break
print('\033[33m<<< ENCERRADO >>>\033[m')
