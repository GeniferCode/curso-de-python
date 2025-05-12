pessoas_nome = []
pessoas_peso = []
leves = []
pesadas = []
while True:
    pessoas_nome.append(str(input('Nome: ')))
    pessoas_peso.append(float(input('Peso: ')))
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas_nome)} pessoas.')
for pos, peso in enumerate(pessoas_peso):
    if peso == min(pessoas_peso):
        leves.append(pessoas_nome[pos])
    elif peso == max(pessoas_peso):
        pesadas.append(pessoas_nome[pos])
print(f'O maior peso lido foi de {min(pessoas_peso)}Kg. Peso de {pesadas}.')
print(f'O menor peso lido foi de {max(pessoas_peso)}Kg. Peso de {leves}.')
