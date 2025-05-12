from ex115.lib.interface import *
from time import sleep
import os

verifica = os.path.exists('arquivo.txt')
if verifica is False:
    with open("arquivo.txt", "x") as file:
        file.write('')
    print('\033[32mArquivo.txt criado com sucesso.\033[m')

while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if escolha == 1:
        titulo('PESSOAS CADASTRADAS')
        exibir()
    elif escolha == 2:
        titulo('CADASTRAR PESSOAS')
        cadastrar()
    elif escolha == 3:
        titulo('Saindo do sistema, até logo!')
        break
    else:
        print('\033[31mERRO: digite uma opção válida!\033[m')
    sleep(2)
