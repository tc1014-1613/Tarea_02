#encoding: UTF-8

# Autor: Oscar Zuñiga Lara, A01654827
# Descripcion: Calcular IVA, Propina y total a pagar de una cuenta


# A partir de aquí escribe tu programa

subtotal = int(input("¿Cuál es el costo de su comida?"))

iva = subtotal*.16
propina = subtotal*.12

print("Subtotal: ", subtotal)
print("Propina: ", propina)
print("IVA: ",iva)
print("Total a pagar: ", iva + propina + subtotal)