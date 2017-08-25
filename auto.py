# encoding: UTF-8

# Autor: Oscar Zuñiga Lara, A01654827
# Descripcion: calcula la distancia que un auto recorre.

# A partir de aquí escribe tu programa
velocidad = input("¿A que velociad se mueve su vehiculo?")
velocidad = int(velocidad)

distancia1 = (velocidad * 6)
distancia2 = (velocidad * 10)
tiempo = (500 / velocidad)

print("Distancia recorrida en 6Hrs: ", distancia1)
print("Distancia recorrida en 10Hrs: ", distancia2)
print("Tiempo para recorrer 500Km: ", tiempo)
