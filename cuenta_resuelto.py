#encoding: UTF-8

# Autor: Jesús Perea Villegas, A01378903
# Descripcion: Calcular la cuenta, IVA y propina de iuna compra

# A partir de aqui escribe tu programa

costoDeLaComida = int(input("Teclea el costo de tu comida"))
propina = costoDeLaComida*0.15
IVA = costoDeLaComida*0.16

costoTotal = costoDeLaComida + propina + IVA

print("El costo de la comida:",costoDeLaComida)
print("La propina que dejará:",propina)
print("Este es el IVA que se le cobrará:",IVA)
print("Este es el costo total que pagará:",costoTotal)
