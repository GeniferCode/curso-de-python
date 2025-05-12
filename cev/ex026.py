frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('Ela aparece a primeira vez na posição', frase.find('A') + 1)
print('A última vez que ela aparece é na posição:', frase.rfind('A')+1)