from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} x', end=' ')
    c -= 1
    if c == 0:
        print(f'= {factorial(n)}')

# da para utilizar for.