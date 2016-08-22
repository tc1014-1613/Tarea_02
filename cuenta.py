#encoding: UTF-8

# Autor: Aldo Fuentes Mendoza, A01373294
# Descripcion: Calcular costo de comida.

# A partir de aqui escribe tu programa

costoComida = float( input("Teclea el costo de tu comida"))

propina = costoComida * .15
iVA = costoComida * .16

costoTotal = costoComida + propina +iVA

print("Costo de la comida: $", costoComida)
print("Propina: $", "%.2f" % propina)
print("IVA: $", "%.2f" % iVA)
print("Total a pagar: $", "%.2f" % costoTotal)
