print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
quantidade_t = int(input('Quantos termos você quer mostrar? '))
r = ra1 = 0
ra2 = 1
c = 0
while c < quantidade_t:
    if r == 0 and ra2 == 1:
        print(f'{r} 🠖 {ra2} 🠖', end=' ')
        c += 2
    r = ra1 + ra2
    print(f'{r} 🠖', end=' ')
    ra1 = ra2
    ra2 = r
    c += 1
print('FIM')