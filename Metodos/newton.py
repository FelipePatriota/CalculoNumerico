#método de Newton
import math # importa a biblioteca math


def f(x): 
  return math.pow(x,3) + math.pow(x,2) - x + 1  #função a ser analisada

def linha(x): 
  return (3*x**2) + (2*x) - 1 #derivada da nossa função

a = -2 #intervalo inicial
e = 0.00001 #precisão
k = 0 #iterações iniciais em 0
x = a #ponto inicial
while abs(f(x)) > e:
  x = x - f(x) / linha(x) #atualiza o ponto inicial
  k=k+1 #atualiza o número de iterações

print("A raiz encontrada foi: ", x) #imprime a raiz
print("O número de iterações foi: ", k) #imprime o número de iterações