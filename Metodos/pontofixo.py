#método do ponto fixo

import math # importa a biblioteca math
import time # importa a biblioteca time

def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1 #função a ser analisada
def phi(x):
  return math.pow(-x,2) - x + 1 #função phi
a = -1 #intervalo inicial
e = 0.00001 #precisão
k = 0 #iterações iniciais em 0

x = a
while abs(f(x)) > e: #loop para encontrar a raiz
  x = phi(x) #atualiza o ponto inicial
  print(x) #imprime o ponto inicial
  k = k + 1 #atualiza o número de iterações
 
print("A raiz encontrada foi: ", x) #imprime a raiz
print("O número de iteraçõesfoi: ",k) #imprime o número de iterações