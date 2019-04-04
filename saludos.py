def tiempoSegundos(horas,minutos,segundos):
    aux1 = horas * 60
    minutos = minutos + aux1
    aux2 = minutos * 60
    segundos = segundos + aux2
    return segundos

def tiempoHoras(segundos):
    minutos = segundos // 60
    segs = segundos % 60
    if minutos > 60 :
        hora = minutos // 60
        minutos = minutos % 60
    return hora, minutos, segs