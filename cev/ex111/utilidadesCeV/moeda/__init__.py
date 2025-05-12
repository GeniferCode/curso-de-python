def aumentar(preco, porcentagem, mostrar=False):
    res = preco + (preco * porcentagem / 100)
    return res if mostrar is False else moeda(res)


def diminuir(preco, porcentagem, mostrar=False):
    res = preco - (preco * porcentagem / 100)
    return res if mostrar is False else moeda(res)


def dobro(preco, mostrar=False):
    res = preco * 2
    return res if mostrar is False else moeda(res)


def metade(preco, mostrar=False):
    res = preco / 2
    return res if mostrar is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco, aumento, desconto):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:    R${moeda(preco)}')
    print(f'Dobro do preço:     R${moeda(dobro(preco))}')
    print(f'Metade do preço:    R${moeda(metade(preco))}')
    print(f'{aumento}% de aumento:     R${moeda(aumentar(preco, aumento))}')
    print(f'{desconto}% de redução:     R${moeda(diminuir(preco, desconto))}')
    print('-' * 30)