#Tupla: es una estructura de datos en python inmutable.

digitos = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
vocales=("A","E","I","O","U")
meses=("enero","febrero","marzo","abril",
      "mayo","junio","julio","agosto",
      "septiembre","octubre","noviembre","diciembre")
genero= ("masculino","femenino")
conexion=("192.168.0.1",3306,"root","mi12345")

print(digitos)
print(vocales)
print(meses)
print(type(digitos))

aux = list(genero)
aux.append ("trans")
genero=tuple(aux)
print(genero)

#Recorido de una tupla
for i in range(len(meses)):
    print(meses[i])

valores=(1, 1, 1 , 2, 3, 4, 5, 6, 7, 8, 9)

#Conteo del numero de coincidencias de un elemneto en la tupla
print(valores.count(1))

#Acceso por indice en donde se almacena un valor dentro de una tupla
print(meses.index("marzo"))


