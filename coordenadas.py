#encoding: UTF-8

# Autor: Ian González Pámanes, A01373302
# Descripcion: Convierte coordenadas cardinales a coordenadas polares.

from math import atan2, pi

# A partir de aqui escribe tu programa

def main():
  
  x = int(input("introduzca coordenada x"))
  y = int(input("introduzca coordenada y"))
  
  R = (x**2 + y**2)**.5
  angulo = atan2(y,x)
  angulo = angulo*180/3.1416

  print ("El vector es:", r, angulo)

main()
