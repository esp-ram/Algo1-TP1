from random import randint
import os

nombresingle = ""

def clear():
    """ "Limpia" la consola
    """
    os.system("cls")

def GraficaMan(oportunidades):
    """Devuelve los dibujos del ahorcado dependiendo de la cantidad de vidas restantes
    oportunidades: oportunidades restantes
    """
    if oportunidades == 6:
        return(" O\n/|\ \n/ \\\n")
    elif oportunidades == 5 :
        return(" O\n/|\ \n/ \n")
    elif oportunidades == 4 :
        return(" O\n/|\ \n")
    elif oportunidades == 3 :
        return(" O\n/| \n")
    elif oportunidades == 2 :
        return(" O\n | \n")
    elif oportunidades == 1 :
        return(" O\n ")
    elif oportunidades == 0 :
        return("0 vidas")
        

def MuestraLetra(original,incompleta,letranueva):
    """devuelve la palabra que contiene las letras acertadas y guiones donde faltan letras
    original: palabra a adivinar
    incompleta: palabra con letras acertadas y guiones(a ser reemplazada por la que devuelva esta funcion)
    letranueva: letra que ingreso el usuario
    """
    a = 0
    for letra in original:
        if letra == letranueva:
            incompleta = incompleta[:a] + letra + incompleta[a+1:]
            a += 1
        else:
            a += 1
    return incompleta


def CuentaAciertos(incompleta):
    """Cuenta cuantos aciertos contiene la palabra ingresada basandose en la cantidad de caracteres que son diferentes de _
    incompleta: palabra que contiene los aciertos(por lo general el resultado de la funcion MuestraLetra)
    """
    aciertos = 0
    for letra in incompleta:
        if letra.isalpha() == True:
            aciertos += 1
    return aciertos


def Juego(adivinar,nombre):
    """juego principal.
    adivinar: palabra a adivinar, elegida por el usuario o de la lista 
    nombre: nombre del jugador
    """
    vidas = 6
    print(nombre,"la palabra tiene",len(adivinar),"letras.")
    palabraguia = ""
    for i in adivinar:
        palabraguia = palabraguia + "_"
    letrausuario = input("Ingrese una letra : ").lower()
    correctas = 0   # N° de letras correctas
    print(adivinar) #TEST -BORRAR-
    yaingresadas = []
    while vidas != 0 and correctas != len(adivinar) :
        if len(letrausuario) != 1:
            letrausuario = input("Ingrese UNA letra : ").lower()
        elif letrausuario.isalpha() == False :
            letrausuario = input("Ingrese una LETRA : ").lower()
        elif letrausuario in yaingresadas:
            """identifica si la letra ingresada ya fue ingresada anteriormente""" 
            print("Esa letra ya fue ingrasada letra ya ingresada")
            print("Las letras que ya ingresaste son :",yaingresadas)
            print("________________________________________________") #separador
            letrausuario = input("ingrese letra : ")
        elif letrausuario in adivinar :
            """identifica si la letra ingresada esta en la palabra a adivinar"""
            yaingresadas.append(letrausuario)
            palabraguia = MuestraLetra(adivinar,palabraguia,letrausuario)
            print("Letra Correcta!!!")
            print(GraficaMan(vidas))
            print(palabraguia)
            print("Estas letras ya fueron ingresadas :",yaingresadas)
            print("________________________________________________") #separador
            correctas = CuentaAciertos(palabraguia)
            if correctas != len(adivinar):
                letrausuario = input("Ingrese una letra : ").lower()
        else:
            """si la letra ingresada no esta en la palabra a divinar ni fue ingresada anteriormente"""
            vidas = vidas - 1
            yaingresadas.append(letrausuario)
            print("Esa letra es incorrecta")
            print(GraficaMan(vidas))
            print(palabraguia)
            print("Las letras ya ingresadas son :",yaingresadas)
            print("________________________________________________") #separador
            if vidas != 0 :
                letrausuario = input("Ingrese una letra : ").lower()
    if vidas == 0 :
        """si el jugador agoto los intentos"""
        print("Oh no!",nombre, "Perdiste")
        print("La palabra era",adivinar)
    else:
        """si el jugador gano el juego"""
        print("Felicidades",nombre, "ganaste !!!")
        
def Replay(modo):
    """pregunta al usuario si desea jugar otra ves"""
    repetir = input("Desea jugar nuevamente? (si/no) :").lower()
    while repetir != "si" and repetir != "no":
        repetir = input("Desea jugar nuevamente? (si/no) :").lower()
    if repetir == "si" and modo == 1 :
        Singleplayer(nombresjugadores[0])
    elif repetir == "si" and modo == 2 :
        Multiplayer()
    elif repetir == "no":
        print("Gracias por jugar")
        

def Singleplayer(nombresingle):
    """modulo de juego para un solo jugador"""
    listapalabras = ["cuaderno","libro","calculadora","reloj","lapicera","botella","auto","lampara","mesa","celular","teclado","pantalla","pared","perro","elefante","aguila","leon","jirafa","ballena","tigre"]
    guess = listapalabras[randint(0,19)] #palabra random
    Juego(guess,nombresingle)
    Replay(1)


def Multiplayer():
    """modulo de juego para dos jugadores"""
    adivinarj1 = input("{} ingresa una palabra para que {} adivine : ".format(nombremulti2,nombremulti1))
    while not adivinarj1.isalpha() :
        adivinarj1 = input("{} ingresa una palabra para que {} adivine : ".format(nombremulti2,nombremulti1))
    clear()
    Juego(adivinarj1,nombremulti1)
    adivinarj2 = input("{} ingresa una palabra para que {} adivine : ".format(nombremulti1,nombremulti2))
    while not adivinarj2.isalpha() :
        adivinarj2 = input("{} ingresa una palabra para que {} adivine : ".format(nombremulit1,nombremulti2))
    clear()
    Juego(adivinarj2,nombremulti2)
    Replay(2)


#programa principal
#nombresingle = ""
"""programa principal. pide al usuario el modo de juego y sus nombres"""


print("Bienvenido")
print("Ingrese un modo de juego")
print("1 jugador => s ")
print("2 jugadores => m")
jugadores = input("Ingrese una opcion : ").lower()
nombresjugadores = []
while jugadores != "s" and jugadores != "m":
    jugadores = input("Ingrese nuevamente una opcion valida(s o m) : ").lower()
if jugadores == "s":
    nombresingle = input("Ingrese su nombre : ")
    nombresjugadores.append(nombresingle)
    Singleplayer(nombresjugadores[0])
elif jugadores == "m":
    nombremulti1 = input("Ingrese el nombre del jugador 1 : ")
    nombremulti2 = input("Ingrese el nombre del jugador 2 : ")
    Multiplayer()
