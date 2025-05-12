pessoas = {'nome': 'Genifer', 'idade': 19, 'sexo': 'F'}
print(f'A {pessoas['nome']} tem {pessoas['idade']} anos.')
pessoas['peso'] = 47.0
for k in pessoas.keys(): # chaves (índices)
    print(k)
for v in pessoas.values(): # valores
    print(v)
for k, v in pessoas.items(): # tudo, chaves + valores
    print(f'{k} - {v}')
del pessoas['sexo']

#brasil = []
#estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
#estado2 = {'uf': 'Bahia', 'sigla': 'BA'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil)
#print(brasil[1])
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil: # e - estado
    for k, v in e.items():
        print(f'{k} - {v}')