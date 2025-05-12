def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: {opcional} mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """
    if show == True:
        for c in range(n, 0, -1):
            if c == 1:
                print('1', end=' ')
            else:
                print(f'{c} x', end=' ')
        print('=', end=' ')
    for c in range(n-1, 0, -1):
        n *= c
    return n


print(fatorial(5, True))