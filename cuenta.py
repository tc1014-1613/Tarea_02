#encoding: UTF-8

# Autor: Manuel Alejandro Bracho Mendoza, A01378897
# Descripcion: Este programa calcula el total de una comida con el porsentaje de propina e iva.

# A partir de aqui escribe tu programa

subtotal=int(input("Porfavor, ingrese su sibtotal a pagar")
propina=subtotal * 1.15 - subtotal
iva=subtotal * 1.16 - subtotal
total=subtotal+iva+propina
print("el subtotal es",subtotal)
print("la propina es de",propina)
print("la iva es de",iva)
print("el total a pagar es de", total)

