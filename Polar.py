 #encoding: UTF-8
  
# Autor: Oswaldo Morales Rodriguez, A01378566
# Conociendo x e y calcular la hipotrnusa y el angulo

from math import atan2, pi
x=int(input("valor de x"))
y=int(input("valor de y"))
r=((x**2)+(y**2))**0.5
ang=atan2(y,x)
z=atan2(y,x)
ang=(180*z)/pi
print("Hipotenusa es",r,"angulo es",ang)