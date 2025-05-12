palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM','PYTHON','CURSO',
            'GRATIS', 'ESTUDAR','PRATICAR','TRABALHAR','MERCADO',
            'PROGRAMADOR','FUTURO')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for c in palavra:
        if c.lower() in 'aeiou':
            print(c.lower(), end=' ')
