#encoding: UTF-8

# Autor: José Javier Rodríguez Mota, A01372812
# Descripcion: Calcula el porcentaje de hombres y mujeres en un grupo.

#Inicio
#Realizamos nuestra función para obtener el porcentaje de un número n en un total t
def obtenerPorcen(n,t):
    porcentaje=n*100/t
    return porcentaje
#Definimos main
def main():
#Pedimos los datos de entrada
    numM=int(input("Mujeres inscritas"))
    numH=int(input("Hombres inscritos"))
#Calculamos el total de alumnos
    total=numH+numM
#Calculamos los porcentajes
    porM, porH= obtenerPorcen(numM,total), obtenerPorcen(numH,total)
#Imprimimos resultados
    print("Total de inscritos",total)
    print("% de mujeres:",porM,"%")
    print("% de hombres:",porH,"%")
#Ponemos en marcha la función
main()
#Fin