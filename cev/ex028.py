import random
print('Computador pensando...')
computador = random.randint(0,5)
print('Computador: escolhi! Duvido você acertar o número que eu escolhi!')
jogador = int(input('Chuto em: '))
if jogador == computador:
    print('\033[32mMiserável! Você acertou :(')
else:
    print('\033[31mErrou, loser! HAHAHA')