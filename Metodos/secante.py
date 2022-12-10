#método da secante

import math # importa a biblioteca math

def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1 #função a ser analisada
def linha(x):
  return (3*x**2) + (2*x) - 1 #derivada da nossa função

a = -1 #intervalo inicial
b = -2 #intervalo final
e = 0.00001 #precisão
k = 0 
x = b 

while abs(f(x)) > e:
   x = (a*f(b) - b*f(a))/(f(b) - f(a)) #atualiza o ponto inicial
   a = b #atualiza o intervalo
   b = x #atualiza o intervalo
   k = k + 1 #atualiza o número de iterações
print("A raiz encontrada foi: ", x) #imprime a raiz
print("O número de iterações foi: ",k) #imprime o número de iterações