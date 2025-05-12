from emoji import emojize
print('\033[33m-=-=-=- BANCO GENINHA -=-=-=-\033[m')
valor = int(input('Quanto deseja sacar: R$'))
cinquenta = valor // 50
valor = valor -  (cinquenta * 50)
vinte = valor // 20
valor = valor - vinte * 20
dez = valor // 10
valor = valor - dez * 10
real = valor // 1
print(f'Total de cédulas de R$50: {cinquenta}\nTotal de cédulas de R$20: {vinte}')
print(f'Total de cédulas de R$10: {dez}\nTotal de cédulas de R$1: {real}')
print('\033[33m-=-\033[m' * 10)
print(f'Volte sempre ao Banco GENINHA! Tenha um ótimo dia! {emojize(":money_mouth_face:", language="alias")}')
