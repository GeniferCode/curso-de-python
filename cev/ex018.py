import math
valor = math.radians(float(input('Digite o valor do ângulo: ')))
cos = math.cos(valor)
sen = math.sin(valor)
tan = math.tan(valor)
print('Cosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(cos, sen, tan))