from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print(f'Quem nasceu em {ano} tem {idade} anos.')
if idade <= 9:
    print('Categoria MIRIM.')
elif idade <= 14:
    print('Categoria INFANTIL.')
elif idade<=19:
    print('Categoria JÚNIOR.')
elif idade <= 24:
    print('Categoria SÊNIOR.')
else:
    print('Categoria MASTER.')