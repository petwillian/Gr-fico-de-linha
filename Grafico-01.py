# passo 1 - importa a biblioteca
import matplotlib.pyplot as plt

#passo 2 - intanciar o objeto figura
fig, ax = plt.subplots() # 1x1

#passo 3 - Definir os dados
indices = [1,2,3,4]
amostra_a = [1,4,2,3]
amostra_b = [2,8,4,6]
amostra_c = [4,16,8,12]

#passo 4 - plotar os dados no axe/eixo(grafico)
ax.plot(indices, amostra_a, label="Amostra A", color = 'blue', marker = 'o')
ax.plot(indices, amostra_b, label="Amostra B", color = 'green', marker = 'o')
ax.plot(indices, amostra_c, label="Amostra C", color = 'red', marker = 'o')

# titulo do grafico
ax.set_title("Titúlo do Gráfico")

# titulo do x
ax.set_xlabel("Label X")

# titulo y
ax.set_ylabel("Label y")

# a legenda
ax.legend()

#passo 5 - apresentar o grafico
plt.show()