import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    print('Não consegui acessar o site pudim.')

else:
    print('Consegui acessar o site pudim.')


# ou

#import requests

#url = 'https://www.pudim.com.br'

#try:
    #resposta = requests.get(url)
    #if resposta.status_code == 200:
        #print(f'Consegui acessar o site pudim.')

#except:
    #print(f'Não consegui acessar o site pudim.')