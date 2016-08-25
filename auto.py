#encoding: UTF-8

# Autor: Carlos E. Carbajal Nogués, A01373264
# Descripcion: Programa que calcula los kilometros recorridos en cierto tiempo, asi como el tiempo que se necesita para recorrer ciertos kilometros


def operaciones(km):
    res1 = km * 6
    res2 = km * 10
    res3 = 500/km
    print "En seis horas habras recorrido:" , res1 , "km"
    print "En diez horas habras recorrido:" , res2 , "km"
    print "Te falta:" , float(res3) , "horas" , "para recorrer 500 km"

operaciones(int(input("¿Cual es tu velocidad?")))
     
