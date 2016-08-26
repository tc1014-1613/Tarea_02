#encoding: UTF-8

# Autor: Karla Valeria Alcántara Duarte A01373164
# Descripcion: Calcular el total de alumnos y el porcentaje de mujeres y hombres.

mujeres = int(input("Número de mujeres inscritas:"))
hombres = int(input("Número de hombres incritos:"))

total = mujeres+hombres
porcentajeM = (mujeres*100)/total
porcentajeH = (hombres*100)/total

print("El total de alumnos es de:",total,"el porcentaje de mujeres:",porcentajeM,"y el porcentaje de hombres:",porcentajeH)
