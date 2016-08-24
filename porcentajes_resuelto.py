#encoding: UTF-8

# Autor: Jesús Perea Villegas, A01378903
# Descripcion: Sacar el porcentaje de hombres y muejeres y el total de personas

# A partir de aqui escribe tu programa

numeroH = int(input("Teclee el numero de hombres en la clase"))
numeroM = int(input("Teclee el numero de mujeres en la clase"))

totalDePersonas = numeroH + numeroM

porcentajeDeHombres = numeroH * 100 / totalDePersonas
porcentajeDeMujeres = numeroM * 100 / totalDePersonas

print("Este es el total de personas",totalDePersonas)
print("Este es el porcentaje de hombres",porcentajeDeHombres)
print("Este es el porcentaje de mujeres",porcentajeDeMujeres)
