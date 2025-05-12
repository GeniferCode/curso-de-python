from random import randint
print('-=-' * 10)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^30}')
print('-=-' * 10)
vitorias = 0
classificacao = ''
while True:
    n = int(input('Diga um valor: '))
    r = str(input('Par ou ímpar? [P/I] ')).upper()
    nc = randint(0,10)
    s = n + nc
    if s % 2 == 0:
        classificacao = 'PAR'
    else:
        classificacao = 'ÍMPAR'
    print(f'Você jogou {n}, o computador jogou {nc}. Total = {s}, que é um valor {classificacao}!')
    if r == 'P' and classificacao == 'PAR' or r == 'I' and classificacao == 'ÍMPAR':
        vitorias += 1
    else:
        break
    print('\033[34mVocê venceu!\033[m\nVamos jogar novamente...')
print(f'\033[31mGAME OVER!\033[m Você venceu {vitorias} vezes.')
