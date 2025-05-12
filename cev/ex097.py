def escreva(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(f'{msg:^{tamanho}}')
    print('-' * tamanho)


escreva('Genifer')
escreva('APRENDENDO PYTHON')
escreva('2025')