import os
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, buscado):
        if nodo is None:
            return None
        if nodo.dato == buscado:
            return nodo
        if buscado < nodo.dato:
            return self.__buscar(nodo.izquierda, buscado)
        else:
            return self.__buscar(nodo.derecha, buscado)

    # Funciones públicas de la clase Arbol
    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)


def menu():
    conta=0
    while conta==0:
        os.system("cls")
        print("Opciones")
        print("1= Insertar")
        print("2= Mostrar en preorden")
        print("3= Mostrar en orden")
        print("4= Mostrar en postorden")
        print("5= Buscar dato")
        print("6= Salir")
        opcion=int(input("\n¿Qué quieres hacer?"))
            
        if opcion==1:
            os.system("cls")
            opc='S'
            while opc == 'S':
                dato = input("Ingresa elemento para agregar al árbol: ")
                arbol.agregar(dato)
                opc = input("   Otro dato? ").upper()
            input("Presiona <<enter>> para continuar")
        elif opcion==2:
            os.system("cls")
            arbol.preorden()
            input("Presiona <<enter>> para continuar")
        elif opcion==3:
            os.system("cls")
            arbol.inorden()
            input("Presiona <<enter>> para continuar")
        elif opcion==4:
            os.system("cls")
            arbol.postorden()
            input("Presiona <<enter>> para continuar")
        elif opcion==5:
            os.system("cls")
            buscado = input("Busca algo en el árbol: ")
            nodo = arbol.buscar(buscado)
            if nodo is None:
                print(f"{buscado} no existe")
            else:
                print(f"{buscado} sí existe")
            input("Presiona <<enter>> para continuar")
        elif opcion==6:
            conta=1
            print("Vas a salir")
            input("Presiona <<enter>> para continuar")
        else:
            print("La opción no es valida")

# PROGRAMA PRINCIPAL
raiz = input("Ingresa el elemento raíz del árbol: ")
arbol = Arbol(raiz) 

menu()

'''
opc='S'
while opc == 'S':
    dato = input("Ingresa elemento para agregar al árbol: ")
    arbol.agregar(dato)
    opc = input("   Otro dato? ").upper()


#Recorrido del arbol  
arbol.preorden()
arbol.inorden()
arbol.postorden()

# Búsqueda de elementos en el arbol
buscado = input("Busca algo en el árbol: ")
nodo = arbol.buscar(buscado)
if nodo is None:
    print(f"{buscado} no existe")
else:
    print(f"{buscado} sí existe")
'''