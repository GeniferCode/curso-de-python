sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250:
    sal = sal + (sal * 0.1)
else:
    sal = sal + (sal * 0.15)
print('Novo salário: {:.2f}'.format(sal))