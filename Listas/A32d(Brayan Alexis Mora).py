#Brayan Alexis Mora Paredes
#Ejercicio 3.2.d ¿Hay más letras “A” o más letras “E” en una cadena? Escribir un programa que lo decida.
def contar(letra,letra2,cadena):
    contador=0
    contador2=0
    for x in cadena:
        if x == letra:
            contador+=1 
        elif x == letra2:
            contador2+=1
        
    if contador > contador2:
        print("La letra ", letra," aparece mas veces que la letra ", letra2,".")
    elif contador2 > contador:
        print("La letra ", letra2," aparece mas veces que la letra ", letra,".")
    else:
        print("La letra ", letra," aparece las mismas veces que la letra", letra2,".")


cadena=input("Ingrese la cadena: ").lower()
letra=input("Ingrese la primera letra ").lower()
letra2=input("Ingrese la segunda letra ").lower()
contar(letra,letra2,cadena)