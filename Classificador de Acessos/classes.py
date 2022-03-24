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
    arq = pd.read_csv('buscas.csv')
    X = arq[['home', 'busca', 'logado']]
    Y = arq['comprou']
    return X, Y
