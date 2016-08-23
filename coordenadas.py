#encoding: UTF-8
# Autor: Adrián E. Téllez López
# Sacar el porcentaje de hombres y mujeres en una clase

import math

# A partir de aqui escribe tu programa

x = int(input("Cual es el valor de x"))
y = int(input("Cual es el valor de y"))

z = (x * x) + (y * y)
magnitud = math.sqrt(z)
grad = math.atan2(y,x)
grad = math.degrees(grad)

print ("Magnitud:", magnitud)
print ("Angulo:", grad, "°")


