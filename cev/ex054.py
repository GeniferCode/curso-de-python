from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = ano_atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos \033[34m{maior}\033[m pessoas maiores de idade e \033[31m{menor}\033[m pessoas menores de idade.')