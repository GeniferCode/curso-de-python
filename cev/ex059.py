from time import sleep
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
r = int(input('Escolha: '))
while r != 5:
    if r == 1:
        s = n1 + n2
        print('Soma:', s)
    elif r == 2:
        m = n1 * n2
        print('Multiplicação:', m)
    elif r == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Maior: ', maior)
    elif r == 4:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
    elif r == 5:
        r = 5
    else:
        print('Opção inválida. Tente novamente.')
    sleep(1)
    r = int(input('Escolha: '))
print('Programa encerrado.')
