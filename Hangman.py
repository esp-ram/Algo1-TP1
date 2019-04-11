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
    else :
        return ("error")

def singleplayer():
    palabras = ["cuaderno","libro","calculadora","reloj","lapicera","botella","auto","lampara","mesa","celular","teclado","pantalla","pared","perro","elefante","aguila","leon","jirafa","ballena","tigre"]
    vidas = 6
    adivinar = palabras[randint(0,19)] #palabra random a adivinar
    print("la palabra tiene",len(adivinar),"letras")
    print(adivinar) #test
    palabraguia = ""
    for i in adivinar:
        palabraguia = palabraguia + "_"
    letrausuario = input("ingrese letra : ")
    corr = 0   # N° de letras correctas
    while vidas != 0 and corr != len(adivinar) :
        if letrausuario in adivinar :  #si letra es correcta
            a = 0
            corr = 0
            for letra in adivinar: #compara las letras ingresadas con las de la palabra a adivinar 
                if letra == letrausuario:
                    palabraguia = palabraguia[:a] + letra + palabraguia[a+1:]
                    a += 1
                else:
                    a += 1
            for l in palabraguia: #cuenta las letras correctas
                if l != "_":
                    corr += 1
            print("Letra Correcta!")
            print(palabraguia)
            print(GraficaHombre(vidas))
            print("________________________________________________") #separador
            if corr != len(adivinar):
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

#programa principal

print("Bienvenido")
jugadores = int(input("Numero de jugadores (1 o 2) :"))
while jugadores < 1 or jugadores > 2:
    print("Solo pueden jugar 1 o 2 jugadores")
    jugadores = int(input("Ingrese nuevamente el numero de jugadores (1 o 2) :"))
if jugadores == 1:
    nombre1 = input("Ingrese su nombre ")
    singleplayer()
elif jugadores == 2:
    nombre1 = input("Ingrese el nombre del jugador 1")
    nombre2 = input("Ingrese el nombre del jugador 2")
else:
    pass