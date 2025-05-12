soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números pares e a soma dos valores PARES digitados foi \033[34m{soma}\033[m.')
