preco_normal = float(input('Informe o valor do produto: R$'))
print("""===== Opções de pagamento =====
1- Dinheiro/cheque
2- Cartão
3- 2x no cartão
4- 3x ou mais no cartão""")
pagamento = int(input('Digite a opção de pagamento: '))
valor = preco_normal
if pagamento == 1:
    valor = preco_normal - (preco_normal * 0.1)
elif pagamento == 2:
    valor = preco_normal - (preco_normal * 0.05)
elif pagamento == 3:
    valor = preco_normal
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = preco_normal + (preco_normal * 0.2)
    valor_parcelas = valor / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcelas} COM JUROS.')
else:
    print('\033[31mOpção inválida.\033[m')
print('Preço a pagar: R${:.2f}'.format(valor))
