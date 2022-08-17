'''
Para obtener ciertas estadísticas de un recorrido, se pide realizar un programa que dada una distancia, entregue la velocidad en kilómetros por hora y en metros por segundo. Para esto, existen dos variables tiempo y distancia que vienen en segundos y kilómetros respectivamente. Tu programa debe guardar en la variable resultado un string.
'''

tiempo = 1 # En s
distancia = 0.01 # En km
v_kmh = distancia/(tiempo/3600) # Velocidad en km/h
resultado = "La velocidad es " + str(v_kmh) + " km/h o " + str(v_kmh*5/18) + " m/s"

print(resultado)
