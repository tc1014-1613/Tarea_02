#encoding: UTF-8

# Autor: Marlon Brandon Velasco Pinello
# Descripcion: Ultimo programa en phyton.

# A partir de aqui escribe tu programa

from math import atan2, pi, sqrt

def main(x,y):
    art=(180*atan2(y,x))/pi
    r = sqrt(((x*x)+(y*y)))
    print("Magnitud =",r)
    print("Angulo =",art)

x=int(input("ingresar el valor de x"))
y=int(input("ingresar el valor de y"))
main(x,y)