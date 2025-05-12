n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
div_int = n1 // n2
div_res = n1 % n2
print('SOMA - {} + {} = {}'.format(n1, n2, soma))
print('SUBTRAÇÃO - {} - {} = {}'.format(n1, n2, sub))
print('MULTIPLICAÇÃO - {} * {} = {}'.format(n1, n2, mul))
print('DIVISÃO - {} / {} = {}'.format(n1, n2, div))
print('POTÊNCIA - {} ** {} = {}'.format(n1, n2, pot))
print('DIVISÃO INTEIRA - {} // {} = {}'.format(n1, n2, div_int))
print('RESTO DE DIVISÃO - {} % {} = {}'.format(n1, n2, div_res))

# precedência
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - + ou -

# print('{:=^20}'.format(nome da variável))
# a variável será escrita centralizada (^) usando a variável mais "=" preenchendo o espaço

print('Olá \nTudo bem?', end=' ')
print('Como você está?')

