soma = 0
valores = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        valores += 1
print(f'A soma dos {valores} valores solicitados deu {soma}.')