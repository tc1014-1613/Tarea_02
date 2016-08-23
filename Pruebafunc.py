
#encoding: UTF-8

#Autor: José Javier Rodríguez Mota
#Descripción: Reproduce notas musicales


#Inicio
from Myro import beep
do4=261.63
re4=293.66
mi4=329.63
fa4=349.23
sol4=392
la4=440
si4=493.88
do5=523.25
re5=587.33
mi5=659.26
fa5=698.46
sol5=783.99
la5=880
si5=987.77
tiempo=0.2
def  reproducir(t,n):
    beep(t,n)
def main():
    reproducir(tiempo,mi5)
    reproducir(tiempo,mi5)
    reproducir(tiempo,mi5)
    reproducir(tiempo,do5)
    reproducir(tiempo,mi5)
    reproducir(tiempo,sol5)
    
main()