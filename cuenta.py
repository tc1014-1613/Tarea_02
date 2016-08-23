#encoding: UTF-8

# Autor: Diego Perez Aka DiegoCodes, A01373737
# Descripcion: CalculaCuentas

# A partir de aqui escribe tu programa ok :)

costo = int(input("Ingrese el costo de su comida"))
print("Calculando costo total...")
subt = costo
propina = costo*0.15
iva = costo*0.16
total = subt+propina+iva
print("Su subtotal es de $",subt)
print("El costo de la propina es de $",propina)
print("El IVA es de $",iva)
print("El costo total es de $",total)
