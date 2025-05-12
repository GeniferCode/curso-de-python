alunos = []
c = 0
while True:
    alunos.append([]) # lista para cada pessoa
    alunos[c].append(str(input('Nome: ')).capitalize())
    alunos[c].append([]) # aqui vai ficar as notas
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos[c][1].append(nota1)
    alunos[c][1].append(nota2)
    alunos[c].append(media)
    r = str(input('Deseja continuar? '))
    if r in 'Nn':
        break
    c += 1
print('-=-' * 10)
print('Indíce      Nome      Média')
print('-=-' * 10)
i = 0
for dado, aluno in enumerate(alunos):
    for pos, info_aluno in enumerate(aluno):
        if pos == 0:
            print(f'{i:^6}{aluno[0]:^16}{aluno[2]:^5}', end=' ')
    i += 1
    print()
while True:
    indice = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if indice == 999:
        print('FINALIZANDO...\n>>>> Volte sempre! <<<<')
        break
    print(f'As notas de {alunos[indice][0]} são {alunos[indice][1]}.')
