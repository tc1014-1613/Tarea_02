#encoding: UTF-8

# Autor: Marlon Brandon Velasco Pinello
# Descripcion: Problerma del automovil en phyton.

# A partir de aqui escribe tu programa

def main(v):
    h6=v*6
    h10=v*10
    km5=500/v
    print ("vas a recorrer en 6 horas",h6,"km")
    print ("vas a recorrer en 10 horas",h10,"km")
    print ("Tardaras",km5,"horas en recorrer 500km")
    
v=int(input("Ingresa tu velocidad actual de km/hora"))
main(v)
