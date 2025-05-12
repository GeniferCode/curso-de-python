valores = []
posmaior = []
posmenor = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(valores)
menor = min(valores)
for pos, v in enumerate(valores):
    if v == maior:
        posmaior.append(pos)
    if v == menor:
        posmenor.append(pos)
print(f'Você digitou os valores: {valores}.')
print(f'O maior valor digitado foi {maior} nas posições {posmaior}.')
print(f'O menor valor digitado foi {menor} nas posições {posmenor}.')
