#Estructura de datos lineales: Arreglos, pilas, colas
#Estrucuturas lineales en python
# *Listas          -list
# *Tuplas          -tuple
# *Diccionarios    -dict
# *Conjunto        -set

#Listas (list)

nombres= ["Eduardo","Misael","Lisbeth","Diana"]
print(nombres)
print(type(nombres))
'''
tupla = tuple(nombres)
print(tupla)
print(type(tupla))
'''
 #Ingresa solo un elemento al final del lista
nombres.append("Eva")
print(nombres)

#Ingresa varias elemnetos tratados como elemntos independientes al final de la lista 
nombres.extend(["Juan Pablo","Maria Fernanda"]) 
print(nombres)

#Insertar un elemento en una posicion n especifica
nombres.insert(0,"Armando")
print(nombres)

nombres.insert(2,"Angelica")
print(nombres)

#Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

#Eliminar un elemento por su indice
nombres.pop(2)
print(nombres)

#Eliminar un elemento segun su valor
nombres.remove("Eduardo")
print(nombres)

#Ordenas la lista
#Ordenar de  forma ascendente
nombres.sort()
print(nombres)

nombres.insert(0,"Zoila")
print(nombres)

nombres.sort()
print(nombres)

#Invertir la lista ---- el orden---reverse()
nombres.reverse()
print(nombres)

#Ordenar la lista en forma descendente: sort(reverse=True)
nombres2= ["Eduardo","Misael","Lisbeth","Diana"]
nombres2.reverse()
print(nombres2)

nombres2.sort(reverse=True)
print(nombres2)

#contar elementos de una lista
nombres2.append("Diana")
print(nombres2)

print(nombres2.count("Diana"))


#Investigar la teoria de pilas y colas, asi como algunas de sus princioales aplicaciones
#Desarrollar un programa que haga el conteo del numero de veces que aparece
#un elemento en una lista, es decir, los mismo que el metodo count().