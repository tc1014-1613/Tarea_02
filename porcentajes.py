#encoding: UTF-8
# Autor: Edgar Eduardo Alvarado Duran,     A01371424
# Problema 4

hombres= int(input("¿Cuantos hombres estan inscritos?"))
mujeres= int(input("¿Cuantas mujeres estan inscritas?"))
inscritos= hombres+mujeres
h= hombres*100
porcientoh= h/inscritos
m= mujeres*100
porcientom= m/inscritos
print ("El total de inscritos son ", inscritos)
print ("El porcentaje de hombres es de ", porcientoh, "%")
print ("El porcentaje de mujeres es de ", porcientom, "%")
