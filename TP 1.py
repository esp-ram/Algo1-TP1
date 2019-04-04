"""

"""
from random import randint


nombre1 = " "
nombre2 = " "
prand = 0
p = -1

palabras = ["cuaderno","libro","calculadora","reloj","lapicera","botella","auto","lampara","mesa","celular","teclado","pantalla","pared","perro","elefante","aguila","leon","jirafa","ballena","tigre"]


jugadores = int(input("Numero de jugadores : "))

"""

if jugadores == 1 or jugadores == 2 :
    if jugadores == 2 :
        nombre1 = input("ingrese nombre de jugador 1 : ")
        nombre2 = input("ingrese nombre de jugador 2 : ")
    elif jugadores == 1 :
        nombre1 = input("ingrese nombre del jugador  : ")
else :
    print("non2")
    
"""    

while p < 0 :
    if jugadores == 2 :
        nombre1 = input("ingrese nombre de jugador 1 : ")
        nombre2 = input("ingrese nombre de jugador 2 : ")
        p = 2
    elif jugadores == 1 :
        nombre1 = input("ingrese nombre del jugador : ")
        p = 1
    else :
        jugadores = int(input("ingrese nuevamente el numero de jugadores : "))
        p = -1