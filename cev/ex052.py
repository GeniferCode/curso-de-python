n = int(input('Digite um número: '))
quantidade = 0
for c in range(1,n+1):
    if n % c == 0:
        quantidade += 1
        print(f'\033[34m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'O número {n} foi divisível {quantidade} vezes.')
if quantidade == 2:
    print('E por isso, ele \033[34mé um número primo\033[m.')
else:
    print('E por isso ele \033[31mNÃO\033[m é um número primo.')
