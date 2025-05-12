n = int(input('Digite um número [999 para parar]: '))
s_n = 0
s = 0
while n != 999:
    s += n
    n = int(input('Digite um número [999 para parar]: '))
    s_n += 1
print(f'Você digitou {s_n} números, e a soma entre eles deu {s}.')
