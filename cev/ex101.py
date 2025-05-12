from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade > 65:
        print(f'Com {idade}: VOTO OPCIONAL')
    elif idade > 18:
        print(f'Com {idade}: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade}: VOTO NEGADO')

nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
