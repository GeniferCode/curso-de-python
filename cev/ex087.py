colunas = [[], [], []]
for c in range(0,9):
    if c < 3:
        colunas[0].append(int(input(f'Digite um valor para [0, {c}] ')))
    elif c > 2 and c < 6:
        colunas[1].append(int(input(f'Digite um valor para [1, {c}] ')))
    elif c > 5 and c < 10:
        colunas[2].append(int(input(f'Digite um valor para [2, {c}] ')))
print(f'\033[31m', '-=-' * 15, '\033[m')
soma = 0
for coluna in colunas:
    for valor in coluna:
        print(f'[ {valor} ]', end=' ')
        if valor % 2 == 0:
            soma += valor
    print()
print(f'\033[31m', '-=-' * 15, '\033[m')
print(f'A soma dos valores pares é {soma}.')
soma_coluna = colunas[0][2] + colunas[1][2] + colunas[2][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')
print(f'O maior valor da segunda linha é {max(colunas[1])}.')
