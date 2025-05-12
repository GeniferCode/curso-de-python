# ajuda interativa

help(print)
print(input.__doc__)

# docstrings - criamos uma documentação para a nossa função

def contador(i, f, p):
    """
    -> Faz uma contagem e imprime na tela
    :param i: onde a contagem se inicia
    :param f: onde a contagem cessa
    :param p: De quanto em quanto a contagem vai
    :return: Não tem
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('Fim')

contador(2,10,2)

help(contador) # agora o help funciona

# parâmetro opcional
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(s)

somar(5,3)


def funcao():
    n1 = 4
    print(f'N1 local vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')

def soma(a=0,b=0,c=0):
    s = a + b + c
    return s


r1 = soma(3,2,5)
r2 = soma(2,2)
r3 = soma(6)

print(f'As somas deram {r1}, {r2} e {r3}.')