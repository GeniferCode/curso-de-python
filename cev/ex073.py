tabela = ('Atlético Mineiro', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians', 'Cruzeiro',
          'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude',
          'Mirasol', 'Palmeiras', 'Bragantino', 'Santos', 'Sport', 'São Paulo', 'Vasco da Gama',
          'Vitória')
print(f'Lista do brasileirão 2025: {tabela}')
print(f'Os 5 primeiros são \033[34m{tabela[0:5]}\033[m')
print(f'Os 4 últimos são \033[31m{tabela[-4:]}\033[m')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'O São Paulo está na {tabela.index('São Paulo') + 1} posição')