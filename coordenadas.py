#encoding: UTF-8

# Autor: Aldo Fuentes Mendoza, A01373294
# Descripcion: Calcular magnitud y angulo a partir de x y y.

# A partir de aqui escribe tu programa

from math import atan2, pi

x = float( input("Valor de x"))
y = float( input("Valor de y"))

angulo = atan2(y, x) * 180 / pi
magnitud = (x**2 + y**2)**.5

print("Magnitud:", "%.2f" % magnitud)
print("Angulo:", "%.2f" % angulo, "grados")