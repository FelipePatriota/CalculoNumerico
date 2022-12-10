#método do ponto fixo

import math
import time

def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1
def phi(x):
  return math.pow(-x,2) - x + 1
a = -1 #intervalo
e = 0.00001
k = 0

x = a
while abs(f(x)) > e: #loop
  x = phi(x)
  print(x)
  k = k + 1
 
print("A raiz encontrada foi: ", x)
print("O número de iteraçõesfoi: ",k)