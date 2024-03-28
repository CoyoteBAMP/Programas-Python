#Brayan Alexis Mora Paredes
#Ejercicio 3.2.e Escribir un programa que cuente cúantas veces aparecen cada una de las vocales en una cadena. 
# No importa si la vocal aparece en mayúscula o en minúscula.

def contar(cadena):
    contador=0
    contador2=0
    contador3=0
    contador4=0
    contador5=0
    for x in cadena:
        if x == "a":
            contador+=1 
        elif x == "e":
            contador2+=1
        elif x == "i":
            contador3+=1
        elif x == "o":
            contador4+=1
        elif x == "u":
            contador5+=1
  
    print("La letra a aparece ",contador,"veces")
    print("La letra e aparece ",contador2,"veces")
    print("La letra i aparece ",contador3,"veces")
    print("La letra o aparece ",contador4,"veces")
    print("La letra u aparece ",contador5,"veces")

cadena=input("Ingrese la cadena: ").lower()
contar(cadena)
