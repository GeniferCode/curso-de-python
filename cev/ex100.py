from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        sleep(1)
        n = randint(1, 10)
        print(n, end=' ')
        lista.append(n)
    print('PRONTO!')


def somaPar(lista):
    s = 0
    for numero in lista:
        if numero % 2 == 0:
            s += numero
    print(f'Somando os valores pares de {lista}, temos {s}.')


numeros = []
sorteio(numeros)
somaPar(numeros)
