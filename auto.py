#encoding: UTF-8
# Autor: Mara Anglica Hernandez Parada, A01169796
# Descripcion: calcular la distancia, velocidad o tiempo de acuerdo a lo que nos dan 
# A partir de aqui escribe tu programa

tiempo=6
velocidad=int(input("Dime a que velocidad iba el auto en km/h"))
distancia=tiempo*velocidad

print ("la distancia que recorrio fue", distancia, "km")

tiempo=10
velocidad=int(input("Dime a que velocidad iba el auto en km/h"))
distancia=tiempo*velocidad

print ("la distancia que recorrio fue", distancia, "km")

distancia=500
velocidad=int(input("Dime a que velocidad iba el auto en km/h"))
tiempo=distancia/velocidad

print ("el tiempo que tardo fue de", tiempo, "hrs")