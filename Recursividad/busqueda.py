""" Búsqueda lineal.
 Si x está en lista devuelve su posición en lista, de lo
 contrario devuelve -1.
"""

#Función del Algoritmo: se recorren uno a uno los elementos de la lista 
#y se los compara con el valor x buscado.
def busqueda_lineal(lista, x):
    i = 0 # i tiene la posición actual en la lista, comienza en 0

 #El ciclo recorre todos los elementos de la lista
    for z in lista:
  
#Si z es igual a x, devuelve el valor de i
        if z == x:
            print (i)
            i = i+1
 #si salió del ciclo sin haber encontrado el valor, devuelve -1
    print (-1)


busqueda_lineal([1, 4, 54, 3, 0, 34, 23, 12], 2)
