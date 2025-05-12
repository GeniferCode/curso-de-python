frase = 'Curso em Vídeo Python'
print(frase)
print(frase[9])
print(frase[9:13+1]) # ele não pega o último caractere. Ele começa no marcado e para no final - 1
print(frase[9:21:2]) # caractere 9 até o 20 (21-1) pulando de 2 em dois.
print(frase[:5]) # do 0 até o 5
print(frase[15:]) # do 15 até o final
print(frase[9::3]) # do 9 até o final pulando de 3 em 3
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0,13))
print(frase.find('deo')) # onde começou o 'deo'
print(frase.find('Geni')) # retorna -1 pq não foi encontrado
print('Curso' in frase) # sim, existe (TRUE)
print(frase.replace('Python','Geni'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase.lstrip())
print(frase.split())
lista = frase.split()
print(lista[3])
print(lista[3][1])
print('-'.join(lista))