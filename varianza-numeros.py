import random
a = int(input("Límite inferior a = "))
b = int(input("Límite superior b = "))
n = 10000
i = 0
lista_numeros = []
while n > 0:
    lista_numeros.append(random.randint(a, b))
    n = n - 1
sum = 0
for item in lista_numeros:
    sum = sum + item
n = len(lista_numeros)
media = sum/n
print("media =", media)
sum_var = 0
for item in lista_numeros:
    sum_var = sum_var + (item-media)**2
var = sum_var/n
print("var =", var)
