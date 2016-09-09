#encoding: UTF-8
# Autor: Oswaldo Morales Rodriguez, A01378566
# Conociendo el numero de hobres y mujeres, dar el total y los porcentajes de hombres y mujeres
  
nohom=int(input("Numero de hombres"))
nomuj=int(input("Numero de mujeres"))
total=nohom+nomuj
phom=(nohom*100)/total
pmuj=(nomuj*100)/total
print("El total son",total,"porcentaje de hombres es",phom,"y el porcentaje de mujeres",pmuj)