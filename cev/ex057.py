sexo = str(input('Sexo [M/F]: ')).upper()
while sexo not in 'FM':
        sexo = str(input('\033[31mVocê digitou errado, tente novamente.\033[m\nSexo [M/F]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso.')