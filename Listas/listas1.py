'''
Lista: Es un tipo de dato básico de Python que permite alamacenar
un vonjunto de valores, los cuales pueden se de diferentes tipos 
Para definir una lista basta con hacer una asignacion a un nombre
de variables con los elementos de dicha lista dentro de corchetes
cuadrados. La lista puede estar vacia al inicializarse.
'''
#Declaración de una lista de elementos
# = []
#print("El tipo de datos de la variable Lista es: ",type(Lista))
#input("\n Presiona <<Enter>> para continuar...")

Lista = [0,1,2,"a","e","Hola",3.1416,["I","II","III"],True]
print("El contenido de la lista es: ",Lista)
print("El numero de elementos en la lista es: ",len(Lista))
input("\n Presiona <<Enter>> para continuar...")

for i in range (len(Lista)):
    print(Lista[i])
    input()

input("\n Presiona <<Enter>> para continuar...")


#Agregar datos a ala lista
dato=input("Ingresa un nuevo dato: ")
Lista.extend([dato])

print("El contenido de la lista es: ",Lista)
input("\n Presiona <<Enter>> para continuar...")

#Elimina del tope de la lista
print("Se va a eliminar un elemento de la lista -- el del tope")
Lista.pop()
print("El contenido de la lista es: ",Lista)
input("\n Presiona <<Enter>> para continuar...")

#Elimina el elemento de un indice especifico
print("Se va a eliminar un elemento en el indice 0 de la lista")
Lista.pop(2)
print("El contenido de la lista es: ",Lista)
input("\n Presiona <<Enter>> para continuar...")

#Eliminar el elemento por su valor 
print("Se va a eliminar un elemento por su valor")
Lista.remove("Hola")
print("El contenido de la lista es: ",Lista)
input("\n Presiona <<Enter>> para continuar...")