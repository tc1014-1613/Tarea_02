#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués, A01373264
#Descripcion: Calcula el total de tu cuenta

#Inicio

sub = float(input("Introduce el subtotal de tu cuenta: "))
iva = sub*.16
prop = sub*.15
total = sub + iva + prop

print "Tu cuenta es de: $" + str(sub)
print "La propina es de: $" + str(prop)
print "El IVA es de: $" + str(iva)
print "Tu total es de: $" + str(total)

#Fin
