#encoding: UTF-8

# Autor: Marina Itzel Haro Hernández, A01373471
# Descripcion: Convierte coordenadas cartesianas a polares

from math import atan2
import math

# A partir de aqui escribe tu programa

x = int(input("Coloca el valor de x"))
y = int(input("Coloca el valor de y"))

r = ((x**2 + y**2)**(1/2))
angulo = math.atan2(y,x)
angulo = math.degrees(angulo)

print ("El valor de r es", r)
print ("El valor del angulo es", angulo, "grados")



