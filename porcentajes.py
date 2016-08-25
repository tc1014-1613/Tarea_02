#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués, A01373264
#Descripcion: Calcula el porcentaje de mujeres y hombres

#Inicio

mujeres = int(input("¿Cuantas mujeres hay? "))
hombres = int(input("¿Cuantos hombres hay? "))
total = hombres+mujeres
porcentaje_h = (hombres*100)/total
porcentaje_m = (mujeres*100)/total
print "Hay un total de:", total, "personas"
print porcentaje_m, "% son mujeres"
print porcentaje_h, "% son hombres"

#Fin
