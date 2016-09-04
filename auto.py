#encoding: UTF-8
# Autor: Adrián E. Téllez López
# Sacar la distancia en 6 y 10hrs, y el tiempo en 500km

v = int(input("Cual es la velocidad en km/h de tu coche"))

d1 = v * 6
d2 = v * 10
t1 = 500/v

print("La distancia que recorres en 6hrs es de", d1, "km")
print("La distancia que recorres en 10hrs es de", d2, "km")
print("El tiempo que tardas en recorrer 500km es de", t1, "hrs")
