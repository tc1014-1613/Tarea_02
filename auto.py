#encoding: UTF-8

# Autor: Karla Valeria Alcántara Duarte A01373164 
# Descripcion:Calcular la distancia y el tiempo que tarda un auto de acuerdo a la velocidad que lleva.

velocidad = int(input("Introduce la distancia en km/hr"))

# v = d/t
distancia1 = velocidad*6
distancia2 = velocidad*10
tiempo = 500/velocidad

print("La distancia que recorre en 6 hrs:",distancia1,"kilometros")
print("La distancia que recorre en 10 hrs:",distancia2,"kilometros")
print("El tiempo en el que recorre 500 km:",tiempo,"horas")


