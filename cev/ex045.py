from random import randint
itens = ['pedra', 'papel', 'tesoura']
computador = randint(0,2)
print('-=-' * 10)
print(f'{'JOKENPÔ': ^30}')
print('-=-' * 10)
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('O que vai jogar? '))
print(f'Computador escolheu {itens[computador]}')
print(f'Jogador escolheu {itens[jogador]}')
if jogador == computador:
    print('EMPATE.')
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('Jogador venceu.')
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('Computador ganhou.')
else:
    print('Opção inválida. Tente novamente.')
