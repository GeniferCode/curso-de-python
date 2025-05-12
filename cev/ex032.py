from datetime import date, datetime

ano = int(input('Digite o ano que deseja analisar ou 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É bissexto. Triste pra tukkkk')
else:
    print('O ano {} não é bissexto. Bom pra tukkk'.format(ano))