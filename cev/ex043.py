altura = float(input('Informe a sua altura em metros: '))
peso = float(input('Informa o seu peso em kilos: '))
IMC = peso / altura**2
print(f'Seu IMC é de {IMC:.1f}.')
if IMC < 18.5:
    print('\033[31mVocê está abaixo do peso.')
elif IMC > 18.5 and IMC < 25:
    print('\033[32mPeso ideal.')
elif IMC >= 25 and IMC <= 30:
    print('\033[33mSobrepeso.')
elif IMC > 30 and IMC <= 40:
    print('\033[31mObeso(a).')
else:
    print('\033[1;31mNÍVEL THAIS CARLA. Obesidade mórbida.')