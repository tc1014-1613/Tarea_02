#encoding: UTF-8

# Autor: José Javier Rodríguez Mota, A01372812
# Descripcion: Un programa que te diga cuanto pagar en un restaurante, contando propina e IVA e imprime desglosado.

#Inicio
#Realizamos la función para calcular porcentajes
def calcular(d,p):
    calculo=d*p/100
    return calculo
#Definimos nuestra función main    
def main():
#Solicitamos el precio de la cuenta
    subt= float(input("¿Cuánto costará la comida?"))
#Realizamos las operaciones correspondientes 
    prop, iva = calcular(subt,15), calcular(subt,16)
#Sumamos
    total= subt+prop+iva
#Imprimimos resultado    
    print("""Costo de la comida: %.2f
Propina: $%.2f
IVA: $%.2f
Total a pagar: $%.2f"""%(subt,prop,iva,total))
#Ponemos en marcha el código
main()
#Fin
