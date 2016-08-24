#encoding: UTF-8

# Autor: Rodrigo García López, A01373670
# Descripcion: Velocidad, distacnias y tiempo

# A partir de aqui escribe tu programa

velocidad = int(input("Inserta la velocidad del auto en kilometros por hora"))
distancia6 = velocidad*6
distancia10 = velocidad*10
tiempo = 500/velocidad
print("La distancia recorrida en 6 horas es ", distancia6, "km")
print("La distancia recorrida en 10 horas es ", distancia10, "km")
print("El tiempo para 500 km es de ", tiempo, "h")
