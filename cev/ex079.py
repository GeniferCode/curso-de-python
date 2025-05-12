valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('\033[31mValor duplicado! Não vou adicionar...\033[m')
    else:
        print('\033[36mValor adicionado com sucesso!\033[m')
        valores.append(num)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
valores.sort()
print(f'Você digitou os valores: {valores}')
