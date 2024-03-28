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

# PROGRAMA PRINCIPAL
raiz = input("Ingresa el elemento raíz del árbol: ")
arbol = Arbol(raiz) 

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