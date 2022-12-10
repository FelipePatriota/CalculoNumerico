#Método da posição falsa
import math
def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1

k = 0
a = -1
b = -2
e = 0.00001

m = (a+b)/2
while abs(f(m) > e):
  m = (a*f(b) - b*f(a))/ (f(b) - f(a))
  if f(a)*f(m) < 0:
    b = m
  else:
    a = m
  k = k + 1

 

  
print("A raiz encontrada foi: ", m)
print("O número de iterações foi: ",k)