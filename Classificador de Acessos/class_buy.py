import csv

def carrega_acessos():
    X = []
    Y = []
    arqv = open('dados.csv', 'r')
    leitor = csv.reader(arqv)
    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append(int(comprou))
    
    return X, Y
