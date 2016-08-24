#encoding: UTF-8

# Autor: Rodrigo García López, A01337670
# Descripcion: Cálculo de ángulo e hipotenusa

from math import atan2, pi
x = int(input("Valor de x: "))
y = int(input("Valor de y: "))
r = (x**2+y**2)**(1/2)
angulo = atan2(y,x)*180/pi
print("Magnitud = ", r)
print("Ángulo = ", angulo)

# A partir de aqui escribe tu programa


