#Hector David Hernandez Rodriguez
#A01374009
#Cuenta restaurante

c=int(input("Introduce el total de la comida"))
IVA=c*(16/100)
P=c*(15/100)
T=c+IVA+P
round(IVA,(2))
round(P,(2))
print("EL precio de la comida es ",c)
print("EL impuesto tiene un total de ",IVA)
print("EL precio del servicio es de ",P)
print("EL percio tota de la comida es ",T)
