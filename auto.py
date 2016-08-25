#encoding: UTF-8

# Autor: Maria Fernanda Rodriguez Hernandes, A01371649
# Descripcion: la distancia en 6 y 10 hrs en m y el tiempo que requiere para recorrer 500km en s.

velocidad = int(input("a que velocidad iba el auto en m/s"))

distancia_6 = velocidad * 360

distancia_10 = velocidad * 600

tiempo = velocidad / 500000

print("la distancia que recorrio en 6 hrs fue de",distancia_6,"m")
print("la distancia que recorrio en 10 hrs fue de", distancia_10,"m")
print("el tiempo que tardo en recorrer 500 km fue de",tiempo,"s")

