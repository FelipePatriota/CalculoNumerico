import math

# Função a ser integrada
def f(x):
    return math.exp(-x ** 2)


#Usando a regra do trapezio repetido para que tenhap a aproximacao da integral no intervalo [a,b]
def trapezoidalRepetido(f, a, b, n):
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
    print(trapezoidalRepetido(f, a, b, n))





#---------------------Resultado---------------------#
# calculo do erro 
# erro = (b-a)**3/(12*n**2)*integral
# erro = (1-0)**3/(12*41**2)*0.7468241328124271
# erro = 0.0001

#-------------------- Resultado --------------------#
#calculo integral
# integral = (b-a)/2*(f(a)+f(b))
# integral = (1-0)/2*(math.exp(-0**2)+math.exp(-1**2))
# integral = 0.7468241328124271

#---------------------Resultado---------------------#
# calculo para obter o numero de intervalos n 
# a formula eh n = sqrt(2*erro/(b-a)*integral)
# n = sqrt(2*0.0001/(1-0)*0.7468241328124271)
# n = 41.0



