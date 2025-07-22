import matplotlib.pyplot as plt
import numpy as np

# Criar um array NumPy com 100 valores, variando de 0 a 10
x = np.linspace(0, 10, 100)
# Aplica a função seno a cada valor de x e armazena no array y1
y1 = np.sin(x)
# Calcula o cosseno de cada valor em 'x' e guarda em 'y2'
y2 = np.cos(x)

# Gráfico de linha
plt.plot(x, y1)
# Rótulos dos eixos 
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
# Título
plt.title('Gráfico de Linha')

# Criação do gráfico de dispersão
plt.scatter(x, y2)
# Adiciona rótulos e título
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico de Dispersão")

# Cria uma lista chamada "valores" com 5 valores inteiros.
valores = [10, 5, 20, 15, 8]
# b. Rótulos para as barras
rotulos = ['A', 'B', 'C', 'D', 'E']
# c. Criando o gráfico de barras
plt.bar(rotulos, valores)
# d. Personalizando o gráfico
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# a. Criando uma figura com dois subplots empilhados verticalmente
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))  # 2 linhas, 1 coluna
# b. Gráfico de linha no primeiro subplot
ax1.plot(valores, rotulos, marker='o', color='blue')
ax1.set_title('Gráfico de Linha')
# c. Gráfico de dispersão no segundo subplot
ax2.scatter(valores, rotulos, color='red')
ax2.set_title('Gráfico de Dispersão')
# d. Personalizando e exibindo
ax1.set_ylabel('Valores Y')
ax2.set_xlabel('Valores X')
ax2.set_ylabel('Valores Y')

plt.tight_layout()  # Ajusta os espaçamentos automaticamente
plt.show()


