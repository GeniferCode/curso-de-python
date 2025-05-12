def leiaInt(n):
    while True:
        try:
            numero = int(input(n.strip()))
            return numero
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar o dado.\033[m')
            return 0
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            n = str('Número inteiro: ')


def leiaReal(n):
    while True:
        try:
            numero = float(input(n))
            return numero
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar o dado.\033[m')
            return 0
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue


n1 = leiaInt('Número inteiro: ')
n2 = leiaReal('Número real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}.')
