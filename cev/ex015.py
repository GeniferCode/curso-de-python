dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km percorridos? '))
preco = (60 * dias) + (km * 0.15)
print('O total a pagar é R${:.2f}.'.format(preco))