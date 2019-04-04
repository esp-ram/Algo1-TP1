from random import randint
from todasvidas import *

palabras = ["cuaderno","libro","calculadora","reloj","lapicera","botella","auto","lampara","mesa","celular","teclado","pantalla","pared","perro","elefante","aguila","leon","jirafa","ballena","tigre"]
randp = 0

def singleplay():
    vidas = 6
    randp = randint(0,19)
    word = list(palabras[randp])
    print("la palabra tiene ",len(word)," letras")
    pidol = input("ingrese letra")
    print(word) #test
    while vidas > 0 :
        if pidol in word :
            print("correcto")
            print(v6(vidas))
            pidol = input("ingrese letra : ")
        else:
            print("incorrecto")
            vidas = vidas -1
            print(v6(vidas))
            pidol = input("ingrese letra : ")
    print("loss")
    
singleplay()