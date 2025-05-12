frase = str(input('Digite uma frase: ')).upper().split()
frase1 = ''.join(frase)
separado = []
for c in range(len(frase1) - 1, -1, -1):
    separado.append(frase1[c])
contrario = ''.join(separado)
print(f'A frase {frase1} ao contrário é {contrario}.')
if frase1 == contrario:
    print('\033[32mE portanto, é palídromo.\033[m')
else:
    print('\033[31mE portanto, não é palíndromo.\033[m')