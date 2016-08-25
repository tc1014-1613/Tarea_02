#encoding: UTF-8

# Autor: Sánchez Iparrazar Allan A01379951
# Descripcion: Convierte coordenadas cartesianas a coordenadas polares
from math import atan2, pi, sqrt

# A partir de aqui escribe tu programa

x = int(input("Introduce el valor del eje X"))
y = int(input("Introduce el valor del eje Y"))

magnitud=sqrt(x**2+y**2)
angulo = (atan2(y,x))*magnitud

print("Magnitud:",magnitud)
print("Ángulo:",angulo)