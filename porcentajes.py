#encoding: UTF-8

# Autor: Rodrigo García López, A01373670  
# Descripcion: Cálculo de género en una clase

# A partir de aqui escribe tu programa

numMujeres = int(input("Mujeres inscritas "))
numHombres = int(input("Hombres inscritos "))
total = numMujeres+numHombres
porHombres = numHombres/total*100
porMujeres = numMujeres/total*100
print("Total inscritos", total)
print("% hombres ", porHombres,"%")
print("% mujeres ", porMujeres, "%")
