nome = str(input('Digite o seu nome completo: '))
print('Em maiúsculo:', nome.upper())
print('Em minúsculo:', nome.lower())
nome1 = len(nome)
espacos = nome.count(' ')
nome2 = nome.split()
print('Quantidade de letras (sem espaço):', nome1-espacos) # ou len(nome) - nome.count(' ')
print('Quantidade de letras do primeiro nome: ', len(nome2[0])) # ou len(nome.find(' ')

