'''
Realice un programa que le pida al usuario un número, y le devuelva la cantidad de dígitos que tiene el número.
'''

numero = int(input("Número = "))

contador = 1 
div_entera = numero // 10

while div_entera != 0:
    contador = contador + 1
    div_entera = div_entera // 10

num_cifras = contador
print("El número tiene", num_cifras, "dígitos.")

