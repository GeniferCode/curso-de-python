from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}.')
if idade > 18:
    print(f'\033[31mVocê já deveria ter se alistado há {idade - 18} anos!')
    print(f'Seu alistamento foi em {ano_atual-(idade - 18)}\033[m')
elif idade == 18:
    print('\033[34mVocê tem que se alistar IMEDIATAMENTE!')
else:
    print(f'\033[32mAinda faltam {18-idade} anos para o alistamento')
    print(f'Você irá se alistar em {ano_atual + (18-idade)}\033[m')