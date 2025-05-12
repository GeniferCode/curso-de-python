t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
qt = 0
while c <= 10:
    qt += 1
    print(f'{t} 🠖', end=' ')
    t += r
    c += 1
print('PAUSA')
i = int(input('Quantos termos deseja mostrar a mais? '))
while i != 0:
    for n in range(0, i):
        qt += 1
        print(f'{t} 🠖', end=' ')
        t += r
    print('PAUSA')
    i = int(input('Quantos termos deseja mostrar a mais? '))
print(f'Progressão finalizada com {qt} termos mostrados.')