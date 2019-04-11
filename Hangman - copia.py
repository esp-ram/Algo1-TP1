from random import randint


def GraficaHombre(oportunidades):
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
        

def LetraCorrecta(original,incompleta,letrauser,vidas):
    incompleta = MuestraLetra(original,incompleta,letrauser)
    correctas = CuentaAciertos(incompleta)
    return (incompleta,correctas,"Letra Correcta",GraficaHombre(vidas))


def MuestraLetra(original,incompleta,letranueva):
    a = 0
    for letra in original: 
        if letra == letranueva:
            incompleta = incompleta[:a] + letra + incompleta[a+1:]
            a += 1
        else:
            a += 1
    return incompleta


def CuentaAciertos(incompleta):
    aciertos = 0
    for letra in incompleta:
        if letra != "_":
            aciertos += 1
    return aciertos


def singleplayer():
    palabras = ["cuaderno","libro","calculadora","reloj","lapicera","botella","auto","lampara","mesa","celular","teclado","pantalla","pared","perro","elefante","aguila","leon","jirafa","ballena","tigre"]
    vidas = 6
    adivinar = palabras[randint(0,19)] #palabra random
    print("la palabra tiene",len(adivinar),"letras")
    print(adivinar) #test
    palabraguia = ""
    for i in adivinar:
        palabraguia = palabraguia + "_"
    letrausuario = input("ingrese letra : ")
    correctas = 0   # N° de letras correctas
    while vidas != 0 and correctas != len(adivinar) :
        if letrausuario in adivinar :  #si letra es correcta
            palabraguia = MuestraLetra(adivinar,palabraguia,letrausuario)
            print(palabraguia)
            correctas = CuentaAciertos(palabraguia)
            print("Letra Correcta!")
            print(GraficaHombre(vidas))
            print("________________________________________________") #separador
            if correctas != len(adivinar):
                letrausuario = input("ingrese letra : ")
        else:   #si letra no es correcta
            print("Letra Incorrecta")
            vidas = vidas - 1
            print(palabraguia)
            print(GraficaHombre(vidas))
            print("________________________________________________") #separador
            if vidas != 0 :
                letrausuario = input("ingrese letra : ")
    if vidas == 0 :
        print("Oh no! Perdiste")
        print("la palabra era",adivinar)
    else:
        print("Felicidades",nombre1, "ganaste !!!")
    repetir = input("Desea jugar nuevamente ? (si/no) ")
    if repetir == "si":
        singleplayer()
    elif repetir == "no":
        print("Gracias por jugar")
        
        
def multiplayer():
    vidasj1 = 6
    vidasj2 = 6
    adivinarj2 = input("{} ingresa una palabra para que {} adivine : ".format(nombre1,nombre2))
    adivinarj1 = input("{} ingresa una palabra para que {} adivine : ".format(nombre2,nombre1))
    letraj1 = input("{} ingresa una letra : ".format(nombre1))
    letraj2 = input("{} ingresa una letra : ".format(nombre2))
    palabraguiaj1 = ""
    palabraguiaj2 = ""
    correctasj1 = 0
    correctasj2 = 0
    for i in adivinarj1 :
        palabraguiaj1 = palabraguiaj1 + "_"
    for j in adivinarj2 :
        palabraguia2 = palabraguiaj2 + "_"
    #???
    while vidasj1 != 0 and vidasj2 != 0 and correctasj1 != len(adivinarj1) and correctasj2 != len(adivinarj2):
        if letraj1 in adivinarj1:
            respuesta = LetraCorrecta(adivinarj1,palabraguiaj1,letraj1,vidasj1)
            for i in range (0,5):
                print (respuesta[i])
            print("________________________________________________") #separador
            if correctasj1 != len(adivinarj1):
                letraj1 = input("{} ingresa una letra : ".format(nombre1))
        else:
            vidasj1 -= 1
            print("Letra incorrecta")
            print(GraficaHombre(vidasj1))
            print("________________________________________________") #separador
            if vidasj1 != 0 :
                letrausuario = input("ingrese letra : ")
            



#programa principal

print("Bienvenido")
print("Ingrese un modo de juego")
print("1 jugador => s ")
print("2 jugadores => m")
jugadores = input("Ingrese una opcion ").lower()
while jugadores != "s" and jugadores != "m":
    jugadores = input("Ingrese nuevamente una opcion valida(s o m) : ")
if jugadores == "s":
    nombre1 = input("Ingrese su nombre : ")
    singleplayer()
elif jugadores == "m":
    nombre1 = input("Ingrese el nombre del jugador 1 : ")
    nombre2 = input("Ingrese el nombre del jugador 2 : ")
    multiplayer()
else:
    pass