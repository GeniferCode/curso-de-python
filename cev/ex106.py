from time import sleep

cores = ('\033[m', # 0 - limpa
         '\033[31m', # 1 - texto vermelho
         '\033[32m', # 2 - texto verde
         '\033[0;46m', # 3 - fundo azul 
         '\033[7;30m' # 4 - fundo branco
         )


def ajuda(com, cor = 0):
    título(f'MANUAL DO COMANDO {com}', 3)
    print(cores[4], end='')
    help(com)
    print(cores[0])
    sleep(2)

def título(msg, cor = 0):
    tam = len(msg) + 4
    print(cores[cor], end= '')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(cores[0])
    sleep(1)

comando = ''    
while True:
    título('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo!', 1)
