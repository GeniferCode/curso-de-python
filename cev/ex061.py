print('Gerador de PA')
print('-=-=-=-=-=-=-')
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(f'{t} 🠖 ', end='')
    t += r
    c += 1
print('FIM')
