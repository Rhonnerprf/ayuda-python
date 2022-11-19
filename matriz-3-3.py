'''
Realiza un programa que capture los valores de una matriz de 3 x 3 y te imprima en la pantalla la suma de la diagonal.
'''

matriz = [[1, 2, 3],
        [4, 5, 6],
        [8, 10, 12]]

sum = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            sum = sum + matriz[i][j]

print(sum)
