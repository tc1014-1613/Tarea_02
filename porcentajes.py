#encoding: UTF-8

# Autor: Aldo Fuentes Mendoza, A01373294
# Descripcion: Calcular porcentaje de hombres y mujeres.

# A partir de aqui escribe tu programa

hombres = int( input("Hombres inscritos:"))
mujeres = int( input("Mujeres inscritas:"))

total = hombres + mujeres

mPorcentaje = mujeres / total * 100
hPorcentaje = hombres / total * 100

print("Total inscritos:",total)
print("Hombres:","%.2f" % hPorcentaje,"%")
print("Mujeres:","%.2f" % mPorcentaje,"%")
