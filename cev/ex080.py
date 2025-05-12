valores = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > max(valores):
        valores.append(n)
        print('Adicionado ao final da lista.')
    if n < min(valores):
        valores.insert(0, n)
        print('Adicionado na posição 0 da lista.')
    if min(valores) < n < max(valores):
        pos = 0
        for posicao in range(pos, len(valores)):
            if n < valores[posicao]:
                valores.insert(posicao, n)
                print(f'Adicionado na posição {posicao} da lista.')
                break
        pos += 1
print(valores)
