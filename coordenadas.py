#encoding: UTF-8

# Autor: Karla Valeria Alcnatara Duarte A01373164
# Descripcion: Calcular magnitud y angulo de un vector.

from math import *

x = int(input("Introduce el valor x"))
y = int(input("Introduce el valor y"))

r = hypot(x,y)
anguloRad = atan2(y,x)
anguloGrad = anguloRad*(180/pi)

print("La magnitud es de:",r,"y el angulo de:",anguloGrad,"grados")


