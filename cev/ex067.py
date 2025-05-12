while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('\033[1;34m-\033[m' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n * c}')
    print('\033[1;34m-\033[m' * 30)
print('Programa TABUADA ENCERRADO. Volte sempre!')
