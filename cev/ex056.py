soma = 0
quant_novinhas = 0
idade_velho = 0
velho = ''
for c in range(1,5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma += idade
    if idade < 20 and sexo == 'F':
        quant_novinhas += 1
    if sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        velho = nome
media = soma / 4
print(f'A média da idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {idade_velho} anos e se chama {velho}.')
print(f'Ao todo são {quant_novinhas} mulheres com menos de 20 anos.')