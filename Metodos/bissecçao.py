#método da bissecção 
import math # importa a biblioteca math


def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1 #função a ser analisada 

k = 0  #iterações iniciais em 0 
a = -2 #intervalo inicial
b = -1 #intervalo final  
e = 0.00001 #precisão 

if f((a+b)/2) < e: #se a raiz for encontrada no meio do intervalo
  print("A raiz encontrada foi: ", (a+b)/2) #imprime a raiz
  
else: #se não, inicia o método da bissecção
  while b - a > e: #enquanto o intervalo for maior que a precisão
    m = (a + b)/2 #calcula o ponto médio
    if f(a)*f(m) < 0: #se o produto for menor que 0, a raiz está no intervalo [a,m]
      b = m #atualiza o intervalo 
    else: #se não, a raiz está no intervalo [m,b]
      a = m #atualiza o intervalo
    k = k + 1 #atualiza o número de iterações

print("A raiz encontrada foi: ", m) #imprime a raiz
print("O número de iterações foi: ", k) #imprime o número de iterações