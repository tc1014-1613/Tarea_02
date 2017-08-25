
#Oscar Zuñiga Lara
#A01654827

#Imicio

#Convierte cordenadas cartesianas a polares.
import math

xval = int(input("¿Cual es el valor de X?"))
yval = int(input("¿Cuál es el valor de Y?"))

r = (xval**2 + yval**2)**0.5
angulo =(math.atan2(yval, xval)) * 180 /math.pi

print("El valor de R es: ", r)
print("El angulo es: ", angulo)
