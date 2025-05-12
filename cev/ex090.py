nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
aluno = {'Nome': nome, 'Média': media}
if media >= 7:
    aluno['Situação'] = '\033[32mAprovado\033[m'
if media < 5:
    aluno['Situação'] = '\033[31mReprovado\033[m'
else:
    aluno['Situação'] = '\033[33mRecuperação\033[m'
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
