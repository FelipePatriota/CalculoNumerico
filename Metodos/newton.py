#método de Newton
import math


def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1
def linha(x):
  return (3*x**2) + (2*x) - 1 #derivada da nossa função

a = -2
e = 0.00001
k = 0
x = a
while abs(f(x)) > e:
  x = x - f(x) / linha(x)
  k=k+1

print("A raiz encontrada foi: ", x) 
print("O número de iterações foi: ", k)