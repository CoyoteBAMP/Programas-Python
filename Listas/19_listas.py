''' Listas: En Python, las listas son uno de los tipos de datos básicos de variables
    para generar una lista solo se requiere asignar a un nombre de variables los elementos 
    que va a contener dentro de corchetes ([]). la lista puede estar basia
'''
import os
digitos = [1,2,3,4,5,6,7,8,9]
vocales = ["a","e","i","o","u"]
arreglo = [] #Se puede declarar una lista vacia

elementos = ["20371004","Ana","Rojas",20,[90,95,90,100],2,True]

os.system ("cls")

print(elementos)

print("Elementos de la lista, un por uno: ")
for i in range (len(elementos)):
    print(elementos[i])
input("Presiona <<enter>> para continuar")

#Agregar elementos a una lista
elementos.extend([90.5])
print(elementos)

nuevo = input("Introduce el nuevo elemento a agregar en la lista: ")
elementos.extend([nuevo])

print(elementos)

#Hacer referencia a segmentos -- Revanadas - slices
print(elementos[0:3])
print(elementos[0:5])