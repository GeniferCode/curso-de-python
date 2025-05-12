def aumentar(preco, porcentagem, mostrar=False):
    res = preco + (preco * porcentagem / 100)
    return res if mostrar else mostrar


def diminuir(preco, porcentagem, mostrar=False):
    preco = preco - (preco * porcentagem / 100)
    if mostrar:
        preco = f'{preco:.2f}'
    return preco


def dobro(preco, mostrar=False):
    preco *= 2
    if mostrar:
        preco = f'{preco:.2f}'
    return preco


def metade(preco, mostrar=False):
    preco /= 2
    if mostrar:
        preco = f'{preco:.2f}'
    return preco


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

