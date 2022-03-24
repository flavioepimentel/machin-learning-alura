from classes import carrega_acessos
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier

X, Y = carrega_acessos()
# Seleciona o modelo de predição
# - O modelo MultinomialNB() 
# tem um output em lista todas as previsões 1 a 1.
modelo = MultinomialNB()
# Separa treino e teste
train_x, test_x, train_y, test_y = train_test_split(
    X, 
    Y, 
    test_size=0.25,
    stratify=Y)
# Treina o modelo
modelo.fit(train_x, train_y)
# Realiza previsões
previsao = modelo.predict(test_x)

# Conferindo a acertividade por detrás dos panos
dif = previsao - test_y
acertos = [d for d in dif if d == 0]
total = len(acertos)
elementos = len(Y)
taxa = total/elementos *100 

print(f"A previsão do modelo é: {taxa}")
#
# Testa acuracidade das previsões de acordo com o estimador Dummy
#
dummy_score = DummyClassifier()
dummy_score.fit(train_x, train_y)
dummy_previsao = dummy_score.score(test_x, test_y) * 100
print(f'A previsão do Dummy foi: {dummy_previsao}' )
