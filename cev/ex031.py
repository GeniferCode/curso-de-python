dis = float(input('Digite a distância da viagem em KM: '))
if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis * 0.45
print('Preço: '.format(preco))