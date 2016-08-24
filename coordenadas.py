#encoding: UTF-8

# Autor: José Javier Rodríguez Mota, A01372812
# Descripcion: Obtener magnitud y dirección de un vector

#Inicio
#Importamos la función arcotangente y pi de la librería de matemáticas
from math import atan2, pi
#Definimos main solamente ya que estamos usando funciones de otra librería
def main():
#Pedimos las coordenadas "x" y "y"
    x=float(input("Valor de x"))
    y=float(input("Valor de y"))
#Realizamos los cálculos    
    magnitud=(x**2+y**2)**0.5
    angulo= atan2(y,x) *180/pi
#Imprimimos resultados
    print("""Magnitud = %f
Ángulo = %f"""%(magnitud,angulo))
#Ponemos en marcha el código
main()
#Fin
