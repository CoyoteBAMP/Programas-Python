def sumarTiempo(hor,min,seg,hor2,min2,seg2):
    hora = hor + hor2
    minu = min + min2
    segg = seg + seg2

    if segg == 60:
        segg = 00
        minu += 1
    
    if minu == 60:
        minu = 00
        hora += 1
    elif minu == 61:
        minu = 1
        hora +=1

    print("La hora resultante es ",hora,":",minu,":",segg)


hora=int(input("Ingrese la hora 1: "))
min =int(input("Ingrese los minutos 1: "))
segun=int(input("Ingrese los minutos 1: "))

hora2=int(input("Ingrese la hora 2: "))
min2 =int(input("Ingrese los minutos 2: "))
segun2=int(input("Ingrese los minutos 2: "))

sumarTiempo(hora,min,segun,hora2,min2,segun2)





