#encoding: UTF-8

# Autor: Diego Perez Villa AKA DiegoCodes, A01373737
# Descripcion:  CalculaPorcentajes

# A partir de aqui escribe tu programa

h = int(input("Cuantos hombres hay inscritos?"))
m = int(input("Cuantas mujeres?"))
t = h+m
ph = (h/t)*100
pm = (m/t)*100
print("Entonces son",t,"? El porcentaje de hombres es", ph,"% y de mujeres",pm,"%")