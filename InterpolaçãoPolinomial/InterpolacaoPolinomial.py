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

w = [20, 25, 30, 35, 40, 45, 50]
z = [0.99907, 0.99852, 0.99826, 0.99818, 0.99828, 0.99849, 0.99878]

# Essa função retorna a matriz de Vandermonde para um conjunto de pontos x, que é utilizada para ajustar um polinômio aos pontos.
def vandermonde_matrix(x, n):
    V = np.zeros((len(x), n+1))
    for i in range(len(x)):
        for j in range(n+1):
            V[i,j] = x[i]**j
    return V 

# Esses são os graus dos polinômios que serão ajustados
grau_p2 = 2
grau_p6 = 6

# Matrizes de Vandermonde para cada conjunto de pontos
V = vandermonde_matrix(x, grau_p2)
D = vandermonde_matrix(w, grau_p6)

# Resolução do sistema para os coeficientes dos polinômios
a = np.linalg.solve(V, y)
c = np.linalg.solve(D, z)


# Impressão dos resultados
print("Esse é o valor para um polinômio de grau 2:", p(32.5, a))
print("Esse é o valor para um polinômio de grau 6:", p(32.5, c))