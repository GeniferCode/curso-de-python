metros = float(input('Digite um valor em metros: '))
print('A medida de {}m corresponde a:'.format(metros))
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(metros/1000, metros/100, metros/10, metros*10, metros*100, metros*1000))
