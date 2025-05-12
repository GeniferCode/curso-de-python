tuplas = (int(input('Digite o 1º número: ')),
        int(input('Digite o 2º número: ')),
        int(input('Digite o 3º número: ')),
        int(input('Digite o 4º número: ')))
print(f'O valor 9 apareceu {tuplas.count(9)} vezes')
if 3 in tuplas:
    print(f'O valor 3 apareceu na posição {tuplas.index(3) + 1}')
else:
    print(f'O valor 3 não apareceu em nenhuma posição')
print(f'Os valores pares digitados foram: ', end=' ')
for n in tuplas:
    if n % 2 == 0:
        print(f'{n}', end=' ')
