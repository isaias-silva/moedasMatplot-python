
#libs
import matplotlib.pyplot as plt
import numpy as np
#modulos
from moedasSigla import MOEDAS_KEYS
import varMoney


dias = input("\ntempo(em dias):")

while (int(dias)>350):
    print("numero de dias muito grande!\n max. 350")
    dias = input("\ntempo(em dias):")

tempo = np.arange(0, int(dias), 1)
for sigla in MOEDAS_KEYS:

    moeda = varMoney.variacao(dias, sigla)
    plt.plot(tempo, moeda)

plt.legend(MOEDAS_KEYS)
plt.xlabel("tempo")
plt.ylabel("moedas")
plt.title("variação do valor de moedas em relação ao real em "+dias+" dias:")
plt.grid()
plt.show()
