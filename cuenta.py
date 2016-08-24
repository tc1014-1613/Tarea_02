#encoding: UTF-8

# Autor: Sánchez Iparrazar Allan A01379951
# Descripión: Calcula el total a pagar, iva y propina de una comida

# A partir de aqui escribe tu programa
total = int(input("Introduce el costo de la comida"))
iva = total*0.16
propina = total*0.15
Total=total+iva+propina
print("Total de la comida: $",total)
print("IVA: $",iva)
print("Propina: $",propina)
print("Total a pagar: $",Total)