import numpy as np
import matplotlib.pyplot as plt

# parâmetros do modelo
beta = 0.4    # coeficiente de transmissão da doença
gamma = 0.035 # taxa de recuperação/cura dos infectados
N = 1000      # população total
S0 = 990      # número inicial de suscetíveis
I0 = 10       # número inicial de infectados
R0 = 0        # número inicial de recuperados
t_max = 60    # tempo total de simulação (em dias)

# equações diferenciais do modelo SIR
def SIR_model(y, t, beta, gamma, N):
    S, I, R = y
    dSdt = -beta/N * S * I
    dIdt = beta/N * S * I - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# método Runge-Kutta de ordem 2
def RK2(f, y0, t0, t_max, h, *args):
    t = [t0]
    y = [y0]
    while t[-1] < t_max:
        k1 = h * np.array(f(y[-1], t[-1], *args))
        k2 = h * np.array(f(y[-1] + k1, t[-1] + h, *args))
        y_next = y[-1] + 0.5 * (k1 + k2)
        t_next = t[-1] + h
        y.append(y_next)
        t.append(t_next)
    return np.array(t), np.array(y)

# resolvendo o modelo SIR
y0 = S0, I0, R0
t0, h = 0, 0.1
t, y = RK2(SIR_model, y0, t0, t_max, h, beta, gamma, N)
S, I, R = y[:,0], y[:,1], y[:,2]

# plotando as curvas S(t), I(t) e R(t)
plt.plot(t, S, label='Suscetíveis')
plt.plot(t, I, label='Infectados')
plt.plot(t, R, label='Recuperados')
plt.xlabel('Tempo (dias)')
plt.ylabel('Número de indivíduos')
plt.title('Modelo SIR')
plt.legend()
plt.show()
