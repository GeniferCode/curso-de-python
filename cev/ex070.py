tot = maisdemil = 0
prodbarato = prod = str(input('Nome do produto: '))
barato = custo = float(input('Preço R$'))
while True:
    if custo < barato:
        prodbarato = prod
        barato = custo
    if custo > 1000:
        maisdemil += 1
    tot += custo
    r = str(input('Quer continuar? [S/N]')).upper()
    if r == 'N':
        break
    prod = str(input('Nome do produto: '))
    custo = float(input('Preço R$'))
print('\033[32m------ FIM DO PROGRAMA ------\033[m')
print(f'O total da compra foi R${tot:.2f}\nTemos {maisdemil} produto(os) custando mais de R$1000,00\nO produto mais barato foi {prodbarato} que custa R${barato:.2f}.')