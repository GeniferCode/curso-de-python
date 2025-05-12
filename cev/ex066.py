soma = quantidade_n = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    quantidade_n += 1
    soma += n
print(f'A soma dos \033[31m{quantidade_n}\033[m valores foi \033[31m{soma}\033[m!')
