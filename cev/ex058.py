from random import randint
computador = randint(0,10)
print('\033[36mCOMPUTADOR:\033[m Pensei em um número entre 0 e 10. Tente adivinhar!')
jogador = int(input('Chuto em: '))
palpites = 0
if jogador != computador:
    palpites += 1
    while jogador != computador:
        print('\033[31mErrou!\033[m')
        if jogador > computador:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais... Tente mais uma vez.')
        jogador =  int(input('Chuto em: '))
        palpites += 1
else:
    palpites += 1
print(f'\033[32mPARABÉNS!\033[m Você acertou com {palpites} tentativa(as).')