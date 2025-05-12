def leiaDinheiro(preco=0):
    valor = 0
    while True:
        v = str(input(f'{preco}')).strip().replace(',','.')
        if v.replace('.', '', 1).isdigit():
            valor = float(v)
            return valor
        else:
            print(f'\033[31mERRO: "{v}" é um preço inválido.\033[m')
