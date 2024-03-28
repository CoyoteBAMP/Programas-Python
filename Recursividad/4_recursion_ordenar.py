def ordenar(lista, cant):
    if cant>1:
        for f in range (0, cant-1):
            if lista[f]>lista[f + 1]:
                aux=lista[f]
                lista[f]=lista[f + 1]
                lista[f + 1]=aux
            ordenar(lista, cant - 1)

datos=[60,44,22,33,2]
print(datos)

ordenar(datos, len(datos))
print(datos)



#Modificar el programa de arborles binarios de manera que sea posible 
#observar un menu de opciones para cada operación a realizar, 
#interactuando con el usuario.

#Modificar el programa compatido de arboles binarios de manera que me 
#permita procesar cadenas de caracteres, por ejemplo (nombres de personas)

#Reporte de programa de ordenamiento en forma recursiva.
#Con prueba de ejecucion en consola y prueba de ejcución en pythontutor.com

#Realizar un resumen del tema de árboles, en base a la pagina de web
# y casos de aplicaion en machine learning


    #Modificar el programa de ordanamiento con funciones recursivas, de manera
    #que se ordene la lista sin utilizar recursividad

    #Elaborar un apunte acerca del tema de recursividad, en base a los 
    #materiales de la plataforma de Moodle

    #Capturar y probar los programa 7

    #Probar el programa de la tarea 1 en la pagina que tenemos pythontutor.com