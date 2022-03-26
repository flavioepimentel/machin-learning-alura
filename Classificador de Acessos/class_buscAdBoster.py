# ====================================================================================
# A otimização de um algoritmo apartir dessa ponto de consistir em três etapas básicas:
#
# 1 - Treinar os modelos
#
# 2 - Comparação de diferentes modelos 
#         - AdaBoostClassifier
#         - MultinomialNB
#         - LinearSVC
#         - SVC
#
# 3 - Testar o modelo com base de dados diferentes e tamanho de amostragens diferentes
#
# =====================================================================================
from classes import carrega_busca
from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB

from sklearn.ensemble import AdaBoostClassifier
modelo = AdaBoostClassifier()


X, Y = carrega_busca()

treino_x, teste_x, treino_y, teste_y = train_test_split(
    X,
    Y,
    test_size=0.1,
    stratify=Y
)

modelo = AdaBoostClassifier()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

# Conferindo a acertividade por detrás dos panos
dif = previsoes - teste_y
acertos = [d for d in dif if d == 0]
total = len(acertos)
elementos = len(teste_y)
taxa = total/elementos * 100 

print(f"A previsão do modelo é: {taxa}")


# Criando um dummy estimator na mão:
qtd_uns = len(Y[Y==1])
qtd_zeros = len(Y[Y==0])
prob_acerto = 100.0 * max(qtd_uns, qtd_zeros) / len(Y)
print(f"A previsão do modelo é: {prob_acerto}")
#========================================
