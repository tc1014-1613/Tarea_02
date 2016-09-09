#encoding: UTF-8
# Autor: Morales Rodriguez Oswaldo, A01378566
# Descripcion: Conociendo la velocidad imprimir cuanto tiempo tardara en recorrer 500 km y la distancia en 6 y 10 hrs
v=int(input("Velocidad que llevaba"))
d1=v*6
d2=v*10
t=500/v
print("La distancia que recorreria en 6 horas es",d1,"kilometros y en 10",d2,"kilometros, le tomaria",t,"horas recorrer 500 km")