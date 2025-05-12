def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.1f}m².')


print('-=-' * 8)
print('   CONTROLE DE TERRENO   ')
print('-=-' * 8)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
