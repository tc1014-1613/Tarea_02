#encoding: UTF-8
# Autor: Edgar Eduardo Alvarado Durán,   A01371424
# Problema 3

cuenta= int(input("Total de su comida"))
propina= cuenta*.15
IVA= cuenta*.16
total= cuenta+propina+IVA
print ("Subtotal de la comida es de $", cuenta)
print ("Propina $", propina)
print ("IVA $", IVA)
print ("Total de su cuenta es de $", total)
