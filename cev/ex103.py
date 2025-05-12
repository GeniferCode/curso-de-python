def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
gol = input('Número de gols: ')
if jogador == '':
    jogador = '<desconhecido>'
if gol == '':
    gol = 0 
ficha(jogador, gol)
