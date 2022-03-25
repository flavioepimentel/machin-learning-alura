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
    ruby = []
    java = []
    algoritmos = []
    for i in arq['busca']:
        if i == 'ruby':
            ruby.append(1)
            java.append(0)
            algoritmos.append(0)
        elif i == 'java':
            ruby.append(0)
            java.append(1)
            algoritmos.append(0)
        elif i == 'algoritmos':
            ruby.append(0)
            java.append(0)
            algoritmos.append(1)
        else:
            ruby.append(0)
            java.append(0)
            algoritmos.append(0)
    arq = arq.assign(ruby=ruby, java=java, algoritmos=algoritmos)
    X = arq[['home', 'logado', 'ruby', 'java', 'algoritmos']]
    Y = arq['comprou']

    return X, Y
