print('-=-' * 10)
print('     CONVERSOR DE BASES')
print('-=-' * 10)
n = int(input('Digite um valor: '))
print("""1 - binário
2 - octal
3 - hexadecimal""")
escolha = int(input('Digite a base de conversão: '))
if escolha == 1:
    print('{} em binário é {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} em octal é {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} em hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')