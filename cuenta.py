#encoding: UTF-8

# Autor: Ian González Pámanes A01373302
# Descripcion: Texto que describe en pocas palabras el problema que estas resolviendo.

# A partir de aqui escribe tu programa
 def main()
  
  total = float(input("Introduzca el total de la comida"))
  
  IVA = total*.16
  propina = total*.15
  
  print("Subtotal", total)
  print("IVA", IVA)
  print("Propina", propina)
  
  print("Total", total+IVA+propina)
  
