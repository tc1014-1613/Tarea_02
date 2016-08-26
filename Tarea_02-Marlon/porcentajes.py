#encoding: UTF-8

# Autor: Marlon Brandon Velasco Pinello
# Descripcion: Problerma del porcentaje hombre y mujer en phyton.

# A partir de aqui escribe tu programa
def main (nh,nm):
    tot=nh+nm
    ph=(100/tot)*nh
    pm=(100/tot)*nm
    print("Total:",tot)
    print("% de hombres:",ph,"%")
    print("% de mujeres:",pm,"%")

nh=int(input("ingresa el numero de hombres"))
nm=int(input("ingresa el numero de mujeres"))
main(nh,nm)
