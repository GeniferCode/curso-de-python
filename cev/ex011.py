altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parade em metros: '))
area = altura * largura
litros = area / 2
print('Você precisará de {} litros de tinta para pintar a parede.'.format(litros))