import math  
import matplotlib.pyplot as plt
import numpy as np

# essa função recebe as funções g1 e g2, e os vetores x e y para calcular os coeficientes a1 e a2
# a1 e a2 são os coeficientes da função phi(x) = a1 + a2*g(x)
def mmq(g_1, g_2, x, y):
    a_1 = 0  
    a_2 = 0
    
    G_11 = np.dot(g_1(x), g_1(x))
    G_12 = np.dot(g_1(x), g_2(x))
    G_21 = np.dot(g_2(x), g_1(x))
    G_22 = np.dot(g_2(x), g_2(x))

    G = [[G_11, G_12], [G_21, G_22]]

    b_1 = np.dot(y, g_1(x))
    b_2 = np.dot(y, g_2(x))

    b = [b_1, b_2]

    a = np.linalg.solve(G, b)
    a_1 = a[0]
    a_2 = a[1]

    return a_1, a_2 


def g_1(r):
    return np.ones(len(r))


def g_2(r):
    return np.sqrt(r)  


def g_3(t):
    return np.log(t)


x = np.array([1, 1.5, 2, 2.5, 3])  
y = np.array([1.6, 5.6, 6, 7.1, 7])  


a_1, a_2 = mmq(g_1, g_2, x, y)
a_3, a_4 = mmq(g_1, g_3, x, y)


def phi(z):
    return a_1 + a_2 * g_2(z)


def phi2(z):
    return a_3 + a_4 * g_3(z)


x_r = np.linspace(1, 3, 100)
x_t = np.linspace(1, 3, 100)

y_r = phi(x_r)
y_t = phi2(x_t)

plt.plot(x, y, 'o')
plt.plot(x_r, y_r, label='Sqrt(x)')
plt.plot(x_t, y_t, label='ln(x)')
plt.legend()
plt.show()

erro = 0
for i in range(len(x)):
    erro += (y[i] - phi(x[i]))**2
print("O erro em sqrt(x) foi:", erro)

erro2 = 0
for i in range(len(x)):
    erro2 += (y[i] - phi2(x[i]))**2
print("O erro em ln(x) foi:", erro2)
