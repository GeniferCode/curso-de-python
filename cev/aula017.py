lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(f'Posição 1 - {lanche[0]}')
lanche.append('cookie')
print(f'{lanche}\nPosição 5 - {lanche[4]}')
lanche.insert(0,'hotdog')
print(f'Posição 1 - {lanche[0]}\nPosição 2 - {lanche[1]}\nPosição 6 - {lanche[5]}')
del lanche[3]
lanche.pop(4)
lanche.remove('hotdog')

num = [5, 7, 2, 8, 3]
num[2] = 9
num.pop() # deleta o último elemento
num.append(3)
num.sort(reverse= True) # reverse = True coloca a lista ordenada do maior para o menor
print(num)
num.pop(1)
print(num)
num.insert(1, 8)
print(num)
if 2 in num:
    num.remove(2)
else:
    print('Não foi encontrado o número 2.')

valores = [] # ou list(), são duas formas de iniciar uma lista vazia
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c}º valor: ')))
for i, v in enumerate(valores):
    print(f'Posição {i} - {v}')
print('Cheguei ao final da lista.')

a = [4, 9, 2, 5]
b = a # cria uma ligação, que fofo :3 o que se altera em uma lista, altera nas duas.
b[2] = 3
print(a)
print(b)
a = [4, 9, 2, 5]
b = a[:] # cria uma cópia, agora b irá receber todos os elementos de a
b[2] = 3
print(a)
print(b)