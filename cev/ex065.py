soma = maior = menor = n = int(input('Digite um número: '))
quantidade_valor_lido = 1
resposta = str(input('Deseja continuar? [S/N] ')).upper()
while resposta != 'N':
    n = int(input('Digite um número: '))
    quantidade_valor_lido += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
media = soma / quantidade_valor_lido
print(f'Você digitou {quantidade_valor_lido} números e sua média foi {media:.2f}.')
print(f'O maior valor lido foi {maior} e o menor foi {menor}.')