#encoding: UTF-8

# Autor: José Javier Rodríguez Mota, A01372812
# Descripcion: Programa que devuelva la distancia que recorre un auto a una velocidad constante en 6 y 10 horas, as como el tiempo que tarda en recorrer 500km 

#Inicio
#Función para obtener distancia recorrida en un tiempo h con una velocidad v
def dis(h,v):
    dist=v*h
    return dist
#Función para obtener tiempo recorrido en un tiempo d con una velocidad v
def ti(d,v):
    tiempo=d/v
    return tiempo
#Definimos nuestra funcin main     
def main():
#Solicitamos la velocidad
    vel= float(input("¿Cuál es la velocidad a la que viaja el auto en km/h?"))
    #Calculamos las variables
    dis6, dis10, tiempo500 = dis(6,vel), dis(10,vel), ti(500,vel)
    #Imprimimos resultados
    print("Distancia recorrida en 6 horas:",dis6,"km")
    print("Distancia recorrida en 10 horas:",dis10,"km")
    print("Tiempo para recorrer 500km:",tiempo500,"horas")
#Ponemos en marcha el código
main()
#Fin