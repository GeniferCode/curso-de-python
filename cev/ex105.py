def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias notas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma 
    """
    qn = len(n)
    media = sum(n) / qn
    maior = max(n)
    menor = min(n)
    dados = {'quantidade de notas': qn, 'maior nota': maior, 'menor nota': menor, 'média da turma': media}
    if sit:
        if media >= 7:
            dados['situação'] = 'boa'
        elif 5 <= media < 7:
            dados['situação'] = 'razoável'
        else:
            dados['situação'] = 'ruim'
    return dados


resp = notas(5.5,6.5,5,3.5, sit=True)
print(resp)
