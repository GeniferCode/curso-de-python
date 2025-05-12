from time import sleep

def maior(* valor):
    m = 0
    print('-=' * 15)
    print('Analisando os valores passados...')
    for c in valor:
        print(c, end=' ')
        sleep(0.5)
        if c > m:
            m = c
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
