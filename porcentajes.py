#encoding: UTF-8

# Autor: Ian González Pámanes, A01373302
# Descripcion: Ingresa el numero de estudiantes masculinos y femeninos, regresa el total y el porcentaje de cada uno.

# A partir de aqui escribe tu programa

def main():
  
  hombres = int(input("Ingrese numero de estudiantes hombres"))
  mujeres = int(input("Ingrese numero de estudiantes mujeres"))
  
  total = hombres + mujeres
  
  print("Total de alumnos:", total, "Porcentaje de hombres:", hombres/total*100, "Porcentaje de mujeres:", mujeres/total*100)
  
main()
