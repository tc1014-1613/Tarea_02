#encoding: UTF-8
# Autor: Adrián E. Téllez López
# Sacar el IVA la propina y el total de una cuenta

# A partir de aqui escribe tu programa

comida = int(input("Cul fue el costo de su comida?"))

propina = comida * 0.15
IVA = comida * 0.16
total = comida + IVA + propina

print("Costo de la comida:", comida,"$")
print("Proina:", propina,"$")
print("IVA::", IVA, "$")
print("Total a pagar:", total,"$")