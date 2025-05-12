def aumentar(preco, porcentagem, mostrar=True):
    preco = preco + (preco * porcentagem / 100)
    if mostrar:
        preco = f'{preco:.2f}'
    return preco


def diminuir(preco, porcentagem, mostrar=True):
    preco = preco - (preco * porcentagem / 100)
    if mostrar:
        preco = f'{preco:.2f}'
    return preco


def dobro(preco, mostrar=True):
    preco *= 2
    if mostrar:
        preco = f'{preco:.2f}'
    return preco


def metade(preco, mostrar=True):
    preco /= 2
    if mostrar:
        preco = f'{preco:.2f}'
    return preco


def moeda(preco):
    preco = f'{preco:.2f}'
    return preco


def resumo(preco, aumento, desconto):
    msg = 'RESUMO DO VALOR'
    print('-' * (len(msg) + 14)) 
    print(f'       {msg}')
    print('-' * (len(msg) + 14))
    print(f'Preço analisado:    R${moeda(preco)}')
    print(f'Dobro do preço:     R${dobro(preco)}')
    print(f'Metade do preço:    R${metade(preco)}')
    print(f'{aumento}% de aumento:     R${aumentar(preco, aumento)}')
    print(f'{desconto}% de redução:     R${diminuir(preco, desconto)}')
    print('-' * (len(msg) + 14))