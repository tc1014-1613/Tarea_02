#encoding: UTF-8

# Autor: Maria Fernanda Rodriguez Hernandes, A01371649
# Descripcion: este es un programa qe calcula el iva la propina y el total de la cuenta de un restaurante .

numero = int(input("Cuntos platillos ordeno? "))
suma = 0
for i in range(1, numero + 1):
    platillo = int(input("Escriba el costo del " + str(i) + "platillo "))
    suma = suma + platillo
    
    iva = suma*.16
    propina = suma*.15
    total= suma +iva+propina

print("el subtotales:",suma,"el iva es:",iva,"la propina es:",propina,"el total es",total)    
                    