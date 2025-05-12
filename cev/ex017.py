from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
# hipotenusa = (co**2 + ca**2)**(1/2)
# jeito que EU faria, usando lógica
print('Valor da hipotenusa: {:.2f}'.format(hypot(co, ca)))