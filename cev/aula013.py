for c in range(0, 6): # ignora o último número, faz de 0 até 5. Repetindo 6 vezes.
    print('Eu te amo muito!')
for c in range(6, 0, -1): #começa do 6 e para no 1 tirando 1 do contador. Para no 1 pq ele ignora o 0.
    print(c)
for c in range(0, 10, 2): # pula de 2 em 2
    print('Bolsonaro e Lula são casados.')
n = int(input('Digite um valor:'))
print('Iniciando a contagem...')
for c in range(0, n+1):
    print(c)