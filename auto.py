#encoding: UTF-8

# Autor: Karla Valeria Alcántara Duarte A01373164 
# Descripcion:Calcular la distancia y el tiempo que tarda un auto de acuerdo a la velocidad que lleva.

velocidad = int(input("Introduce la distancia en km/hr"))
tiempo1 = 6
tiempo2 = 10
# v = d/t
distancia1 = velocidad*tiempo1
distancia2 = velocidad*tiempo2
distancia = 500
tiempo = distancia/velocidad

print("La distancia que recorre en 6 hrs:",distancia1,"kilometros")
print("La distancia que recorre en 10 hrs:",distancia2,"kilometros")
print("El tiempo en el que recoree 500 km:",tiempo,"horas")


