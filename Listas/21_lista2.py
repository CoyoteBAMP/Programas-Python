lista=[1,2,3,4,5]
print(lista)

lista.append(6) #Ingresa solo un elemento al final del lista
print(lista)

lista.extend([7,8]) #Ingresa varias elemnetos tratados como elemntos independientes al final de la lista 
print(lista)

#Insertar un elemento en una posicion n especifica
lista.insert(0,100)
print(lista)

#Eliminar el ultimo elemento de la lista
lista.pop()
print(lista)

#Eliminar un elemento por su indice
lista.pop(0)
print(lista)

#Eliminar un elemento segun su valor
lista.remove(2)
print(lista)