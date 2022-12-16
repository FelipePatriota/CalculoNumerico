def soma_elementos_matriz(matriz): # soma os elementos de cada linha da matriz
  resultado = [] # lista vazia

  # percorre as linhas da matriz
  for i in range(len(matriz)):
      soma = 0
        # percorre as colunas da matriz
      for j in range(len(matriz[i])):
            soma += matriz[i][j]
      resultado.append(soma)
  return resultado