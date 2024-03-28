#Brayan Alexis Mora Paredes
#Ejercicio 3.2.c Escribir una función contar(x, s) que cuente cuántas veces aparece un carácter x dado en una cadena s.

def contar(letra,cadena):
    contador=0
    for x in cadena:
        if x == letra:
            contador+=1    
    print("La letra ", letra," aparece ", contador, " veces.")


cadena=input("Ingrese la cadena: ").lower()
letra=input("¿Cual letra quiere contar? ").lower()
contar(letra,cadena)



