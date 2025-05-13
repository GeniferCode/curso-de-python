def linha(tam=42):
    return '-' * tam


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} -\033[m \033[36m{item}\033[m')
        c += 1
    print(linha())
    escolha = leiaint('\033[32mSua opção: \033[m')
    return escolha

def leiaint(n):
    while True:
        try:
            numero = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        else:
            return numero


def exibir():
    dados = []
    with open("arquivo.txt", "r") as file:
        conteudo = file.readlines()
    for linha in conteudo:
        dados.append(linha.strip().split(';'))
    for pos, dado in enumerate(dados):
       print(f'{dado[0]:<10}{dado[1]:>25} anos')


def cadastrar():
    nome = str(input('Nome: '))
    idade = leiaint('Idade: ')
    with open("arquivo.txt", "a") as file:
        file.write(f'{nome};{idade}\n')
    print(f'\033[32mNovo registro de {nome} adicionado.\033[m')

