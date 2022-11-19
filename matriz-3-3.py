'''
Realiza un programa que capture los valores de una matriz de 3 x 3 y te imprima en la pantalla la suma de la diagonal.
'''

fila = []
matriz = []
dimension = 3

for i in range(dimension):
    for j in range(dimension):
        fila.append(input("Elemento " + str(i+1) + str(j+1) + " :"))
    matriz.append(fila)
    fila = []

sum = 0
for i in range(dimension):
    for j in range(dimension):
        if i == j:
            sum = sum + float(matriz[i][j])

print("Matriz =", matriz)
print("La suma de los elementos de la diagonal es", sum)
