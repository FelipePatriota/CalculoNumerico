import math

# Função a ser integrada
def f(x):
    return math.exp(-x ** 2)


#Usando a regra do trapezio repetido para que tenhap a aproximacao da integral no intervalo [a,b]
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  #Subintervalos
    x = [a + i * h for i in range(n + 1)] # pontos x_i
    y = [f(x_i) for x_i in x]   # pontos y_i

    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])
    return integral

# Fazer a chamada da funcao
if __name__ == '__main__':
    a = 0
    b = 1
    n = 41
    print(trapezoidal_rule(f, a, b, n))
