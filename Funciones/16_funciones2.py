import os

#Una funcion resive argumentos
def bienvenida (usuario):
    print("Hola, bienvenido a python ", usuario)
    print("\nAhora estas a punto de salir de una función")
    input("Presiona <<Enter>> para salir")


#Aqui inicia el programa principal del python
os.system("cls")
nombre=input("¿Cual es tu nombre? ")
bienvenida(nombre) 