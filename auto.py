#encoding: UTF-8

# Autor: José Javier Rodríguez Mota, A01372812
# Descripcion: Programa que devuelva la distancia que recorre un auto a una velocidad constante en 6 y 10 horas, as como el tiempo que tarda en recorrer 500km 

#Inicio
#Solicitamos la velocidad
def dis(h,v):
    dist=v*h
    return dist
def ti(d,v):
    tiempo=d/v
    return tiempo
def main():
    vel= float(input("¿Cuál es la velocidad a la que viaja el auto en km/h?"))
    #Calculamos las variables
    dis6 = dis(6,vel)
    dis10= dis(10,vel)
    tiempo500=ti(500,vel)
    #Imprimimos resultados
    print("Distancia recorrida en 6 horas:",dis6,"km")
    print("Distancia recorrida en 10 horas:",dis10,"km")
    print("Tiempo para recorrer 500km:",tiempo500,"horas")

main()
#Fin