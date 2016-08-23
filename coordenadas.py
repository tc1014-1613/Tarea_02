#encoding: UTF-8

# Autor: Diego Perez Aka DiegoCodes, A01373737
# Descripcion: CalculaAngulosyMagnitudes

from math import *

# A partir de aqui escribe tu programa

xx = int(input("Ingrese la coordenada x"))
yy = int(input("Ingrese la coordenada y"))
print("Advertencia")
ang0 = (atan2(yy,xx))*180/pi

if ang0 < 0:
 ang0 += 360
 
mag = sqrt( xx**2 + yy**2)
    
print("Su angulo es de ",ang0,"Y su magnitud es de",mag)