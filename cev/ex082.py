numeros = list()
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Continua? [S/N] '))
    if r in 'Nn':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Valores digitados: {numeros}')
print(f'Pares: \033[33m{pares}\033[m')
print(f'Impares: \033[34m{impares}\033[m')
