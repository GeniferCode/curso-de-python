from random import randint
from  time import sleep

jogos = []
print(f'\033[32m{'=' * 30}\n{'JOGA NA MEGA SENA':^30}\n{'=' * 30}\033[m')
sorteios = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, sorteios):
    jogos.append([])
    for i in range(0, 6):
        n = randint(0, 60)
        while n in jogos[c]:
            n = randint(0, 60)
        jogos[c].append(n)
    jogos[c].sort()
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(1)
print(f'{'\033[32m'}{'BOA SORTE!':~^30}{'\033[m'}')
