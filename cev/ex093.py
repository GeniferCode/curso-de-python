dados = {}
gols = []
dados['nome'] = str(input('Nome do jogador: '))
q_part = int(input(f'Quantas partidas {dados['nome']} jogou? '))
for c in range(0, q_part):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-=-' * 20)
print(dados)
print('-=-' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'O jogador {dados['nome']} jogou {q_part} partidas.')
for i, v in enumerate(gols):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados['total']} gols.')
