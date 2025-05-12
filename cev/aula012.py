from emoji import emojize

nome = str(input('Qual é o seu nome? '))
if nome == 'Genifer':
    print(emojize('Que nome lindo! :red_heart:', variant='emoji_type'))
elif nome == 'Gustavo':
    print('Que legal! Meu namorado se chama assim.')
elif nome == 'Maria' or nome == 'João':
    print('Seu nome é bem comum.')
print('Bom dia, {}!'.format(nome))