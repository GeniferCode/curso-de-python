n = list()
r = 's'
while r in 'Ss':
    n.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] '))
if 5 in n:
    pos = n.index(5) + 1
n.sort(reverse = True)
print('-=-=-==-=-==-=-===-=-=-==-=-=-=-=-=-=-=')
print(f'Foram digitados {len(n)} valores.')
print(f'A lista na ordem decrescente: {n}.')
if 5 in n:
    print(f'O valor 5 faz parte da lista, aparecendo a primeira vez na posição \033[36m{pos}\033[m.') # posição normal, sem ser python
else:
    print('O valor 5 não está na lista.')