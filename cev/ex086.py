colunas = [[], [], []]
for c in range(0,9):
    if c < 3:
        colunas[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
    elif c > 2 and c < 6:
        colunas[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
    elif c > 5 and c < 10:
        colunas[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
for coluna in colunas:
    for valor in coluna:
        print(f'[{valor: ^5}]', end=' ')
    print()
