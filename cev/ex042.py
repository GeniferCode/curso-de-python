r1 = float(input('Segmento 01: '))
r2 = float(input('Segmento 02: '))
r3 = float(input('Segmento 03: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('\033[32mEles podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Triângulo ISÓSCELES')
    else:
        print('Triângulo ESCALENO.')
else:
    print('\033[31mNão podem formar um triângulo.')