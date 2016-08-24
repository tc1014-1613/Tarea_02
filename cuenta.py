#encoding: UTF-8

# Autor: Marina Itzel Haro Hernández, A01373471
# Descripcion:  Calcula la propina, el IVA y el total a pagar de la comida segun su costo

# A partir de aqui escribe tu programa

def main():
    costoTotalDeLaComida = float(input("Costo total de la comida"))
    propina = costoTotalDeLaComida * 0.15
    IVA = costoTotalDeLaComida * 0.16
    totalAPagar = costoTotalDeLaComida + propina + IVA
    print("El costo total de la comida es", costoTotalDeLaComida, "pesos")
    print("La propina es", propina, "pesos")
    print("El IVA es", IVA, "pesos")
    print("El total a pagar es", totalAPagar, "pesos")

main() 