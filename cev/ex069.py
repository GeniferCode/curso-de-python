homens = mulheres_novas = maiores_idade = 0

while True:
    print('\033[31m-' * 20)
    print(f'{'CADASTRE UMA PESSOA':^20}')
    print('-' * 20, '\033[m')

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    if idade >= 18:
        maiores_idade += 1
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1
    if sexo == 'M':
        homens += 1

    r = str(input('Deseja continuar? [S/N]: ')).upper()
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).upper()
    if r == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'Quantidade de maiores de idade: \033[36m{maiores_idade}\033[m')
print(f'Quantidade de homens: \033[36m{homens}\033[m')
print(f'Quantidade de mulheres com menos de 20 anos: \033[36m{mulheres_novas}\033[m')
