import csv
import pandas as pd
def carrega_acessos():
    X = []
    Y = []
    arqv = open('dados.csv', 'r')
    leitor = csv.reader(arqv)
    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append(int(comprou))
    
    return X, Y

def carrega_busca():
    arq = pd.read_csv('Classificador de Acessos/buscas.csv')
    # arq = arq[['ruby', 'java', 'algoritmos']]
    # for i in arq['busca']:
    #     if i == 'ruby':
    #         arq['ruby'] == 1
    #         arq['java'] == 0
    #         arq['algoritmos'] == 0
    #     elif i == 'java':
    #         arq['ruby'] == 0
    #         arq['java'] == 1
    #         arq['algoritmos'] == 0
    #     elif i == 'algoritmos':
    #         arq['ruby'] == 0
    #         arq['java'] == 0
    #         arq['algoritmos'] == 1
    #     else:
    #         arq['ruby'] == 0
    #         arq['java'] == 0
    #         arq['algoritmos'] == 0

    X = arq[['home', 'logado']]
    Y = arq['comprou']

    return X, Y
