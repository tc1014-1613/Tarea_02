#encoding: UTF-8

# Autor: Marina Itzel Haro Hernández, A01373471
# Descripción: Calcula el total de alumnos y el porcentaje de hombres y mujeres de acuerdo a la cantidad de hombres y mujeres.

# A partir de aqui escribe tu programa

def main():
    mujeres = float(input("Número de mujeres inscritas en clase"))
    hombres = float(input("Número de hombres inscritos en clase"))
    totalDeAlumnos = mujeres + hombres
    porcentajeMujeres = (mujeres*100)/totalDeAlumnos
    porcentajeHombres = (hombres*100)/totalDeAlumnos
    
    print("El total de alumnos inscritos en clase es", totalDeAlumnos)
    print("El porcentaje de mujeres en clase es", porcentajeMujeres, "%")
    print("El porcentaje de hombres en clase es", porcentajeHombres, "%")
    
main()