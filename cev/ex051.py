print('-=-' * 10)
print(f'{'RAZÃO DE UMA P.A': ^30}')
print('-=-' * 10)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r
for c in range(n, decimo + 1, r):
    print(f'{c} \033[31m🠖\033[m', end=" ")
print('Acabou!')