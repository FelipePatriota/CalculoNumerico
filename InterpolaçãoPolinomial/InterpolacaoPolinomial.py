import numpy as np

# Essa função calcula o valor de um polinômio para um determinado valor de x, dado seus coeficientes armazenados em uma lista.
def p(x, a):
    r = 0
    n = len(a)
    for i in range(0, n):
        r += a[i] * (x**i)
    return r

# Nesses trechos, são definidos os conjuntos de pontos para os quais serão ajustados polinômios.
x = [30, 35, 40]
y = [0.99826, 0.99818, 0.99828]

x2 = [20, 25, 30, 35, 40, 45, 50]
y2 = [0.99907, 0.99852, 0.99826, 0.99818, 0.99828, 0.99849, 0.99878]

# Essa função retorna a matriz de Vandermonde para um conjunto de pontos x, que é utilizada para ajustar um polinômio aos pontos.
def vandermonde_matrix(x, n):
    V = np.zeros((len(x), n+1))
    for i in range(len(x)):
        for j in range(n+1):
            V[i,j] = x[i]**j
    return V 

# Qual a temperatura tal que o calor específico é 0.99837? Use uma interpolação linear. para graus celsius
def find_temperature(c, x2, y2):
    n = len(x2)
    V = vandermonde_matrix(x2, n-1)
    a = np.linalg.solve(V, y2)
    for i in range(n-1):
        if y2[i] <= c <= y2[i+1]:
            t = x2[i] + (c - y2[i]) * (x2[i+1] - x2[i]) / (y2[i+1] - y2[i])
            return t
    return None

# Esses são os graus dos polinômios que serão ajustados
grau_p2 = 2
grau_p6 = 6

# Matrizes de Vandermonde para cada conjunto de pontos
V = vandermonde_matrix(x, grau_p2)
D = vandermonde_matrix(x2, grau_p6)

# Resolução do sistema para os coeficientes dos polinômios
a = np.linalg.solve(V, y)
c = np.linalg.solve(D, y2)


# Impressão dos resultados
print("Esse é o valor para um polinômio de grau 2:", p(32.5, a))
print("Esse é o valor para um polinômio de grau 6:", p(32.5, c))
print("Essa é a temperatura para um calor específico:%.2f" % find_temperature(0.99837, x2, y2), "°C")


