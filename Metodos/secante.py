#método da secante
import math
def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1
def linha(x):
  return (3*x**2) + (2*x) - 1
a = -1
b = -2
e = 0.00001
k = 0
x = b
while abs(f(x)) > e:
   x = (a*f(b) - b*f(a))/(f(b) - f(a))
   a = b
   b = x
   k = k + 1
print("A raiz encontrada foi: ", x)
print("O número de iterações foi: ",k)