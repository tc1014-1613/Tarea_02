 #encoding: UTF-8
  
 # Autor: tuNombreCompleto, tuMatricula
 # Descripcion: Texto que describe en pocas palabras el problema que estas resolviendo.
 # Autor: Morales Rodriguez Oswaldo, A01378566
 # Descripcion: Conociendo el subtotal, conocer la propina, IVA y gran
subtotal=int(input("Subtotal de la comida"))
propina=subtotal*0.15
iva=subtotal*0.16
total=subtotal+propina+iva
print("El subtotal es",subtotal, "la propina es",propina,"El IVA es",iva, "total completo es",total)