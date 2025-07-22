# 1. Importe a biblioteca NumPy
import numpy as np

# 2. Crie um array unidimensional chamado arr com os números de 1 a 10
arr = np.arange(1, 11)

# 3. Crie uma matriz bidimensional chamada matriz com dimensões 3x4, preenchida com números inteiros de 1 a 12
matriz = np.arange(1, 13).reshape(3, 4)

# 4. Imprima o array arr e a matriz matriz (RESULTADOS IMPRESSOS NO PASSO Nº12)
# print("Array unidimensional (arr):")
# print(arr)

# print("\nMatriz bidimensional (matriz):")
# print(matriz)

# 5. Acesse o elemento “5” do array arr e o elemento “8” da matriz matriz
elemento_arr = arr[4]           # Índice 4 corresponde ao número 5
elemento_matriz = matriz[1, 3]  # Segunda linha, quarta coluna (índice 1, 3)

# 6. Crie um novo array chamado arr_slice com os elementos de índice 2 a 6 (exclusivo)
arr_slice = arr[2:6]

# 7. Realize uma operação matemática (multiplicação por 2) em todos os elementos do array arr
arr_resultado = arr * 2

# 8. Calcule a soma de todos os elementos da matriz
soma_matriz = matriz.sum()

# 9. Calcule a média dos elementos do array arr
media_arr = arr.mean()

# 10. Crie a transposta da matriz matriz
matriz_transposta = matriz.T

# 11. Concatene o array arr com o array arr_slice
arr_concatenado = np.concatenate((arr, arr_slice))

# 12. Imprima os dados obtidos
print("\n--- Resumo dos dados obtidos ---")
print(f"arr: {arr}")
print(f"matriz:\n{matriz}")
print(f"Elemento 5 do arr: {elemento_arr}")
print(f"Elemento 8 da matriz: {elemento_matriz}")
print(f"arr_slice: {arr_slice}")
print(f"arr_resultado: {arr_resultado}")
print(f"Soma da matriz: {soma_matriz}")
print(f"Média do arr: {media_arr}")
print(f"matriz_transposta:\n{matriz_transposta}")
print(f"arr_concatenado: {arr_concatenado}")