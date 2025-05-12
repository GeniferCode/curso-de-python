from emoji import emojize
cores = {'padrao':'\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m'}
valor_casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual o seu salário mensal: R$'))
anos = int(input('Em quantos anos você irá pagar? '))
prestacao = valor_casa / anos / 12
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f} por mês e você ganha R${:.2f} por mês.'.format(valor_casa, anos, prestacao, salario))
if prestacao > salario * 0.3:
    print('{}Empréstimo NEGADO.'.format(cores['vermelho']))
else:
    print('{}Empréstimo APROVADO. {}'.format(cores['verde'], emojize(':red_heart:', variant='emoji_type')))