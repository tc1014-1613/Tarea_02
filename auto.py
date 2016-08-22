#encoding: UTF-8

# Autor: Aldo Fuentes Mendoza, A01373294
# Descripcion: Calcular distancia viajada a 6 y 10 horas, y tiempo para recorrer 500 km.

# A partir de aqui escribe tu programa

vel = float( input("Teclea la velocidad del auto en km/h"))

dist6hrs = vel * 6
dist10hrs = vel * 10
t500km = 500 / vel

print("Distancia recorrida en 6 horas:",dist6hrs,"km")
print("Distancia recorrida en 10 horas:",dist10hrs,"km")
print("Tiempo para recorrer 500 km:",t500km,"horas")
