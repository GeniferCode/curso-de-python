n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('{} é o maior.'.format(n1))
elif n2 > n1:
    print('{} é o maior.'.format(n2))
else:
    print('\033[34mOs dois são iguais.')