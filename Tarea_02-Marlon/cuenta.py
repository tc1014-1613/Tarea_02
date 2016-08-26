#encoding: UTF-8

# Autor: Marlon Brandon Velasco Pinello
# Descripcion: Problerma de la cuenta.

# A partir de aqui escribe tu programa

def main(cta):
    pro = cta * 0.15
    iva = cta * 0.16
    tot = cta + pro + iva
    print("Costo de la comida: $",cta)
    print("Propina: $",pro)
    print("IVA: $",iva)
    print("Total a pagar: $",tot)
cta=float(input("Valor de tu cuenta"))
main(cta)
