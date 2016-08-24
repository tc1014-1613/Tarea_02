#encoding: UTF-8

# Autor: Marina Itzel Haro Hernández, A01373471
# Descripcion: Calcula la distancia recorrida en 6 y 10 horas y el tiempo en 500 km de un auto de acuerdo a la velocidad

# A partir de aqui escribe tu programa
def main():
    velocidad = float(input("Introduce la velocidad a la que viaja un auto en km/h"))
    distancia1 = velocidad*6
    distancia2 = velocidad*10
    tiempo = 500/velocidad
    print("La distancia que recorre el auto en 6 horas es", distancia1, "km")
    print("La distancia que recorre el auto en 10 horas es", distancia2, "km")
    print("El tiempo que tarda en recorrer el auto en 500 km es", tiempo, "horas")

main()     

# Solucion
