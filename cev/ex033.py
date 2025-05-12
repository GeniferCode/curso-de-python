a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
c = int(input('Mais um: '))
if b<a>c:
    maior = a
elif a<b>c:
    maior = b
else:
    maior = c
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c
print('Maior: {}\nMenor: {}'.format(maior, menor))