def l():
    print('-=-' * 10)

def contador(* num):
    tamanho = len(num)
    print(tamanho)


def soma(a, b):
    s = a + b
    print(s)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

contador(21, 3, 2)
contador(2, 1)
contador(7)
l()
soma(5, 8)
l()

valores = [21, 7, 13, 2]
dobra(valores)
print(valores)