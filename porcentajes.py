#encoding: UTF-8
# Autor: Adrián E. Téllez López
# Sacar el porcentaje de hombres y mujeres en una clase

# A partir de aqui escribe tu programa

hombres = int(input("Cuantos hombres hay inscritos en la clase"))
mujeres = int(input("Cuantas mujeres hay inscritos en la clase"))

total = hombres + mujeres
Porcentajeh = (hombres * 100)/total
Porcentajem = (mujeres * 100)/total

print ("Hay", total, "personas en la clase")
print ("El porcentaje de hombres en la clase es:", Porcentajeh, "%")
print ("El porcentaje de mujeres en la clase es:", Porcentajem, "%")