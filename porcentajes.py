#encoding: UTF-8

# Autor: Sánchez Iparrazar Allan A01379951
# Descripcion: Porcentaje de hombres y mujeres que hay en una clase

# A partir de aqui escribe tu programa
NH = int(input("¿Cuántos hombres hay en la clase?"))
NM = int(input("¿Cuántas mujeres hay en la clase?"))

NT=NH+NM
PH=(NH/NT)*100
PM=(NM/NT)*100

print("Número total de alumnos:",NT)
print("Porcentaje de hombres:", PH,"%")
print("Porcentaje de mujeres:", PM,"%")
