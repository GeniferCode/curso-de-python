expressao = str(input('Digite a expressão: '))
abriu = expressao.count('(')
fechou = expressao.count(')')
if abriu == fechou:
    print('Tudo certo com a expressão.')
else:
    print('Isso está errado, irmãokkk')