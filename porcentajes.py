
#encoding: UTF-8

# Autor: Oscar Zuñiga Lara, A01654827
# Descripcion: Calcula el total de hombres y mujeres, asi como su porcentaje.


# A partir de aquí escribe tu programa

hombres = int(input("¿Cuántos hombres hay?"))
mujeres = int(input("¿Cuántas mujeres hay?"))

total = hombres + mujeres

print("Total: ",total)
print("Porcentaje en Hombres: ", hombres/total*100,"%")
print("Porcentaje en Mujeres: ", mujeres/total*100,"%")