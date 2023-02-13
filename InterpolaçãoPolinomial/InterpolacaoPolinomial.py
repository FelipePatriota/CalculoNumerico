import numpy as np

# Tabela de valores experimentais de calor específico
temperaturas = np.array([20, 25, 30, 35, 40, 45, 50])
calor_especifico = np.array([0.99907, 0.99852, 0.99826, 0.99818, 0.99828, 0.99849, 0.99878])

# Função para interpolação polinomial usando eliminação gaussiana
def interpola_polinomial(x, y, x_val):
    n = len(x)
    A = np.zeros((n, n))
    b = np.zeros(n)
    for i in range(n):
        b[i] = y[i]
        for j in range(n):
            A[i, j] = x[i] ** (n - j - 1)
    # Resolução do sistema por eliminação gaussiana
    x = np.linalg.solve(A, b)
    y_val = 0
    for i in range(n):
        y_val += x[i] * x_val ** (n - i - 1)
    return y_val

# Cálculo do polinômio de grau 2
x_val = 32.5
p2 = interpola_polinomial(temperaturas, calor_especifico, x_val)
print("Polinômio de grau 2:", p2)