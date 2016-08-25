#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogues, A01373264
#Descripcion: Calcula la hipotenusa y los grados de un vector

#Inicio
from math import atan2, pi, hypot, degrees
x = int(input("Longitud de X: "))
y = int(input("Longitud de Y: "))
mag = hypot(x,y)
ang = atan2(y,x)
angu = degrees(ang)
print "Su magintud es de:", mag
print "El angulo vale:" , angu


