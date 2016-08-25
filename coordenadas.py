#Hector David Hernandez Rodriguez
#A01374009
#COORDENADAS
from math import atan2,pi
from math import sqrt

x=int(input("Introduce el valor de x "))
y=int(input("introduce el valor de y "))
T=atan2(y,x)
Tan=round(T,(2))
An=(1/Tan)
r=(x*x)+(y*y)
R=sqrt(r)
R1=round(R,(0))
print("el valor del angulo es ",T)
print("el valor del angulo es ",An)
print("el valor de r es ",R1)
