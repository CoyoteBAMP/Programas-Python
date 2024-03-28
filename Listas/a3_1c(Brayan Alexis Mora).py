def contLetrasPalabras(cadena):
    cont=0
    num=0
    for caracter in cadena:
        cont+=1

        if caracter == " ":
            cont-=1
            if cont == 5:
                num+=1
            cont=0
    if cont == 5:
        num+=1
        
    print("El numero de palabras que tiene 5 letras son: ",num)

cadena = input("Ingresa la cadena: ")
contLetrasPalabras(cadena)