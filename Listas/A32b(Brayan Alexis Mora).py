#Brayan Alexis Mora Paredes
#Ejercicio 3.2.b Queremos contar cuántas letras “A” hay en una cadena x.

cadena= input("Introduce la cadena: ").lower()

contador=0
for x in cadena:
    if x == "a":
        contador+=1

print("La letra a aparece ", contador, " veces.")
