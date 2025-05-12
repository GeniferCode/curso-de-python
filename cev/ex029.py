velocidade = int(input('Digite a velocidade: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mVocê foi MULTADO!\nMulta: R${:.2f}'.format(multa))
else:
    print('\033[32mTudo certo, continue respeitando o limite da velocidade.')