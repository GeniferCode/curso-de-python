nome = str(input('Qual é o seu nome? '))
if nome == 'Genifer':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Parabéns!') if media >= 6 else print('Estude mais!')