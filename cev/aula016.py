lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(f'{lanche[0]}')
print(f'{lanche[-4]}')
print(f'{lanche[0:2]}')
for comida in lanche: # se não precisar de posição
    print(f'{comida}')

for c in range(0,len(lanche)):
    print(f'{c}º - {lanche[c]}')

for pos, comida in enumerate(lanche):
    print(f'{pos}º - {comida}')

print(sorted(lanche)) # sorted coloca a tupla em ordem alfabética

a = (1, 2, 3)
b = (3, 2)
c = a + b # a ordem altera o resultado
print(c)
print(len(c))
print(c.count(9))
print(c.index(3)) # mostra a posição da primeira ocorrência
print(c.index(3, 3))

person = 'Geni', 19, 'F', 46
del(person) # tuplas são imutáveis, somente podemos deletá-las
print(person)