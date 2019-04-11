from random import randint
from todasvidas import *

palabras = ["cuaderno","libro","calculadora","reloj","lapicera","botella","auto","lampara","mesa","celular","teclado","pantalla","pared","perro","elefante","aguila","leon","jirafa","ballena","tigre"]
randp = 0

def singleplay():
    vidas = 6
    randp = randint(0,19)  #seed random
    word = list(palabras[randp]) #palabra random 
    print("la palabra tiene ",len(word)," letras")
    #print(word) #test
    ah = []
    for i in word:
        ah.extend(["_"])
    pidol = input("ingrese letra : ")
    corr = 0   # N° de letras correctas
    while corr < len(word) and vidas > 1 :
        if pidol in word :  #si letra es correcta
            a = 0
            while a < len(word):
                for i in word :   #print a letras acertadas
                    if i == pidol:
                        ah[a] = pidol
                        a = a + 1
                        corr = corr + 1
                    elif i != "_":
                        a = a + 1
                    else:
                        ah[a] = "_"
                        a = a + 1
            print("correcto")
            print(v6(vidas))
            print(ah)
            if corr != len(word):
                pidol = input("ingrese letra : ")
        else:   #si letra no es correcta
            print("incorrecto")
            vidas = vidas - 1
            print(v6(vidas))
            print(ah)
            pidol = input("ingrese letra : ")
    if vidas < 2 :
        print("pierde")
        print("la palabra era ",word)
    else:
        print("gana")
singleplay()
