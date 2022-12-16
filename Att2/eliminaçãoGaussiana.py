def soma_elementos_matriz(matriz): # soma os elementos de cada linha da matriz
  resultado = [] # lista vazia

  # percorre as linhas da matriz
  for i in range(len(matriz)):
      soma = 0
        # percorre as colunas da matriz
      for j in range(len(matriz[i])):
            # soma os elementos
            soma += matriz[i][j] 
      resultado.append(soma)
  return resultado


def eliminacao_gauss(A, b):
  n = len(b)

  # Escalonamento
  for k in range(0, n-1):
      for i in range(k+1, n):
          m = A[i][k]/A[k][k]
          for j in range(k, n):
            A[i][j] = A[i][j] - m*A[k][j]
          b[i] = b[i] - m*b[k]

  # Substituição regressiva
  x = [0] * n
  for i in range(n-1, -1, -1):
      s = b[i]
      for j in range(i+1, n):
          s = s - A[i][j]*x[j]
      x[i] = s/A[i][i]
  return x

# função para criar uma matriz de Hilbert
def hilbert(a, z):
    return [[1 / (i + j + 1) for j in range(z)] for i in range(a)]  

