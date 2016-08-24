#encoding: UTF-8

# Autor: Rodrigo García López, A01373670
# Descripcion: Cálculo de la cuenta restaurante

# A partir de aqui escribe tu programa

costoInicial = int(input("Costo de su comida: "))
propina = costoInicial*0.15
iva = costoInicial*0.16
total = costoInicial + propina + iva
print("Costo de la comida: $%5.2f" % costoInicial)
print("Propina: $%5.2f" % propina)
print("IVA: $%5.2f" % iva)
print("Total a pagar: $%5.2f" % total)