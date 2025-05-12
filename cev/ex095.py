dados = {}
gols = []
time = []
while True:
    dados['nome'] = str(input('Nome do jogador: ')).capitalize()
    q_part = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    for c in range(0, q_part):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    gols.clear()
    r = str(input('Quer continuar? [S/N] ')).upper()[0]
    while r not in 'SN':
        print('\033[31mERRO!\033[m Digite S ou N.')
        r = str(input('Quer continuar? [S/N] '))
    if r == 'N':
        break
print('-=-' * 20)
print(f'{'cod':<3}{'nome':^15}{'gols':^20}{'total':<10}')
print('-' * 60)
for i, jogador in  enumerate(time):
    print(f'{i:<3}{jogador['nome']:^15}{jogador['gols']}{jogador['total']:>10}')
while True:
    r = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if r == 999:
        break
    while r > len(time):
        print(f'\033[31mERRO!\033[m Não existe jogador com o código {r}')
        r = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    print(f'-- LEVANTAMENTO DO JOGADOR {time[r]['nome']}:')
    for jogo, gol in enumerate(time[r]['gols']):
        print(f'   No jogo {jogo + 1} fez {gol} gols.')
print('<< VOLTE SEMPRE >>')
