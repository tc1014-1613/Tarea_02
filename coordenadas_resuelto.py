#encoding: UTF-8

# Autor: Jesús Perea Villegas, A01378903
# Descripcion: Calcular el angulo y su maginitud

from math import atan2, pi

# A partir de aqui escribe tu programa

valorDeX = int(input("Teclea el valor de x"))
valorDeY = int(input("Teclea el valor de y"))

magnitud = ((valorDeX**(2))+(valorDeY**(2)))**(1/2)
angulo = atan2(valorDeX,valorDeY)
print("Tu maginitd es",magnitud)
print("Angulo",angulo)