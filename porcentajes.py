#encoding: UTF-8

# Autor: Maria Fernanda Rodriguez Hernandes, A01371649
# Descripcion: este programa calcula el porcentaje de alumnos y alumnas que hay inscritos en la clase 

alumnos = int(input("cuantos alumnos hay inscritos?"))
alumnas = int(input("cuantas alumnas hay inscritos?"))

total = alumnos + alumnas

porcent_alumno = alumnos*100/total
porcent_alumna = alumnas*100/total

print("el total de almnos inscritos es de",total)
print("el porcentaje de alumnos es de",porcent_alumno,"%")
print("el porcentaje de alumnas es de",porcent_alumna,"%")